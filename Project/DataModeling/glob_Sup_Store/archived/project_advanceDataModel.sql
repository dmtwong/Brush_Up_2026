DROP TABLE globalSuperStore.cust;
DROP TABLE globalSuperStore.orders;
DROP TABLE globalSuperStore.prod;
DROP TABLE globalSuperStore.ship;
DROP TABLE orders_raw.orders;
DROP DATABASE orders_raw;
DROP DATABASE globalSuperStore;
/*
A csv file fit for importing was created by converting the
xlsx file using R, as the file is a large table that needed to be 
fruther spilted into a few tables that satisfy database normalization,
a database 'orders_raw' is created to load the file into a new table 
called 'orders'  
UPDATE: 
Row 1669 contains the value "Fès-Boulemane". The accented character è (\xc3\xa8) is likely the culprit. 
UTF-8 may not be good enough and stop or "silent fail" when it hits the first non-ASCII character it doesn't understand.
UPDATE (2026-02-03 20:02): From current table ship structure,
1) * rowID (now shipID) is the only unique key, not even order ID
2) * orderID has multiply count (up to 14 in 1 case) while 
3) * ShippingCost remain different,
4) checking distinct shipDate group by order ID shows that 
5) * shipDate shipMode City State Country (and possibly postalCode Market Region) follow shipID not orderID
Fruther more when checking city+state+country, 
6) 'Market' is not unique (few cases has 2 distint market EMEA +EU or EMEA + APAC)
7) so as 'Region', mix of Central and EMEA
In that case we can't seperate a table for location using city state country as PK or region + market 
UPDATE (2026-02-05 10:37): 
1) from same orderID there could be multi values for shipDate
2) Using city + state could be PK for Country but not state, market and postal code; maybe an overkill to create a seperate table;
Looking at table 'orders', some fields in current table have multi values for 1 orderID by observation
these columns will be shift to table 'prod' (if prodID is unquie but it is not a good idead after looking 'prod') 
OR table 'ship' (if prodID is not unquie):
Discount, Profit, Quantity, Sales
3) looking at prod table, there's one prodID has two subcategory. In real life may contact source owner to decide whether it deserve a new prodID or merging
but for practice purpose I will simply drop the three rows, 
4) for prodName in table 'prod' there are too many duplicates I will put it in table ship
5) So far 
- shift Discount, Profit, Quantity, Sales from orders to ship
- shift prodName to ship
let's look at table 'cust'
6) distinct custName and Segment value for particular custID, simply make unqiue is good enough 
*/
CREATE DATABASE Orders_raw;
USE Orders_raw;
-- import file, turns out 'row id' and 'discount' contain non integer values and many records were not included
-- change all data type to text and import again and will adjust it after fruther inspection
-- Update instead of LOAD DATA INFILE
-- Update 2: by default a malicious server cannot read files from computer. 
-- to avoid 3948, Enable on Server, then on Client. RESTORE on server side once it's done.
 
SET GLOBAL local_infile = 1;
/*
1) MySQL Command Line: Launch your connection with the flag included: mysql --local-infile=1 -u your_username -p
2) MySQL Workbench:
Go to Database > Manage Connections.
Select your connection.
Go to the Advanced tab.
In the Others box, add: OPT_LOCAL_INFILE=1 (or check the box for "Enable Local Infile" if visible in your version).
3) Python (mysql-connector): When creating your connection object, add the argument: conn = mysql.connector.connect(..., allow_local_infile=True)
*/
TRUNCATE TABLE orders_raw.orders;
DELIMITER // 
LOAD DATA LOCAL INFILE 'C:/Users/mingt/Downloads/Orders2.csv' 
INTO TABLE orders_raw.Orders
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES //
DELIMITER ;

SELECT count(*) from orders_raw.orders; -- 51290
SELECT * FROM orders limit 5;
SET GLOBAL local_infile = 0;

/* Now change the data type
*/
ALTER TABLE `orders_raw`.`orders`
CHANGE COLUMN `Category` `Category` VARCHAR(25) NOT NULL ,
CHANGE COLUMN `City` `City` VARCHAR(50) NOT NULL ,
CHANGE COLUMN `Country` `Country` VARCHAR(50) NOT NULL ,
CHANGE COLUMN `Customer ID` `custID` VARCHAR(9) NOT NULL ,
CHANGE COLUMN `Customer Name` `custName` VARCHAR(50) NOT NULL ,
CHANGE COLUMN `Market` `Market` VARCHAR(10) NOT NULL ,
CHANGE COLUMN `Order Date` `orderDate` VARCHAR(20) NOT NULL ,
CHANGE COLUMN `Order ID` `orderID` VARCHAR(16) NOT NULL ,
CHANGE COLUMN `Order Priority` `orderPriority` VARCHAR(15) NOT NULL ,
CHANGE COLUMN `Postal Code` `postalCode` VARCHAR(10) NULL ,
CHANGE COLUMN `Product ID` `prodID` VARCHAR(30) NOT NULL ,
CHANGE COLUMN `Product Name` `prodName` VARCHAR(150) NOT NULL ,
CHANGE COLUMN `Region` `Region` VARCHAR(20) NOT NULL ,
CHANGE COLUMN `Row ID` `rowID` INT NOT NULL ,
CHANGE COLUMN `Segment` `Segment` VARCHAR(30) NOT NULL ,
CHANGE COLUMN `Ship Date` `shipDate` VARCHAR(20) NOT NULL ,
CHANGE COLUMN `Ship Mode` `shipMode` VARCHAR(30) NOT NULL ,
CHANGE COLUMN `State` `State` VARCHAR(50) NULL ,
CHANGE COLUMN `Sub-Category` `SubCategory` VARCHAR(25) NOT NULL ,
CHANGE COLUMN `Discount` `Discount` DOUBLE NOT NULL ,
CHANGE COLUMN `Profit` `Profit` DOUBLE NOT NULL ,
CHANGE COLUMN `Quantity` `Quantity` INT NOT NULL ,
CHANGE COLUMN `Sales` `Sales` DOUBLE NOT NULL ,
CHANGE COLUMN `Shipping Cost` `ShippingCost` DOUBLE NOT NULL ;

SELECT * FROM orders_raw.orders limit 5;
/* No warnings from altering the table data types, date format issue also seems good 
MySQL expects dates in the ISO standard YYYY-MM-DD format, 
the csv is using DD/MM/YYYY format, to avoid error 1175,
temporarily disable safe update in order to update the two 
date columns and then revert back the safe update setting  

SET SQL_SAFE_UPDATES = 0;
UPDATE orders
SET orderDate = STR_TO_DATE(orderDate, '%d/%m/%Y');
UPDATE orders
SET shipDate = STR_TO_DATE(shipDate, '%d/%m/%Y');
SET SQL_SAFE_UPDATES = 1;
SELECT * FROM orders limit 5;
SHOW COLUMNS FROM orders;
*/ 

/*
Now create another database 'globalSuperStore', 
and then create a table for product 'cust' using the raw table,
custID, custName, Segment should be relevant but 
orderID and rowID is included for preliminary analysis 
(will do the same for 'prod', 'ship', 'order', 
and rowID may be used as PK for ship unless it's not fitted (will create surrogate key in that case) 
custID, custName, Segment, orderID, rowID
*/
CREATE DATABASE globalSuperStore;
USE globalSuperStore;
SHOW COLUMNS FROM orders_raw.orders;

CREATE TABLE globalSuperStore.cust AS
SELECT custID, custName, Segment, orderID, rowID
FROM orders_raw.orders;
/*
Now create table 'prod 
Recall:
custID, custName, Segment, orderID, rowID (cust)
Note after doing a quick groupby + count & then filter one prodid with multi record 
certain column like market, quantity and discount should belong to 'orders' (not 'cust')
prodID, prodName, Category, SubCategory, orderID, rowID (orderID, rowID is included as 'cust') 
*/
CREATE TABLE globalSuperStore.prod AS
SELECT prodID, prodName, Category, SubCategory, orderID, rowID
FROM orders_raw.orders;

/*
Now create table 'ship' and 'order'
Recall:
custID, custName, Segment, orderID, rowID (cust 3 + 2)
prodID, prodName, Category, SubCategory, orderID, rowID (prod 4 + 2)
Following col are included (9 + 2, or 10 + 1): 
shipDate, shipMode, ShippingCost, City, State, Country, postalCode, Market, Region, orderID, rowID 
Follwing for table 'order' (7 + 1)
orderID, orderDate, orderPriority, Discount, Profit, Quantity, Sales, rowID 
*/
CREATE TABLE globalSuperStore.ship AS
SELECT shipDate, shipMode, ShippingCost, City, State, Country, postalCode, Market, Region, orderID, rowID 
FROM orders_raw.orders;

/*
CREATE TABLE globalSuperStore.order AS
SELECT orderID, orderDate, orderPriority, Discount, Profit, Quantity, Sales, rowID 
FROM orders_raw.orders;
*/
/*
Forgot to include FK or order table to link all other tables, 
recreate and rename is as orders to avoid confusion with ORDER clause
*/
DROP TABLE IF EXISTS globalSuperStore.order;
CREATE TABLE globalSuperStore.orders AS
SELECT orderID, orderDate, orderPriority, Discount, Profit, Quantity, Sales, prodID, custID, rowID 
FROM orders_raw.orders;

/* Now explore ship, particularly see whether rowID is good enough as PK
orginally plan to use write a procedure, but can be doing so using R much quicker:
df %>% summarise(across(everything(), n_distinct))
*/
-- expect 1936 (revised: 51290 instead) records 
SELECT count(*) from orders_raw.orders;
SELECT count(*) from ship; 
SELECT count(*) from orders;
SELECT count(*) from prod; 
SELECT count(*) from cust;  
-- SELECT count(rowID) from ship;
SELECT * from ship limit 3;
SELECT count(distinct(rowID)) from ship;
SELECT count(distinct(orderID)) from ship; -- 25035
-- DROP PROCEDURE countDistincy;
/* 
As rowID is unquie but orderID not (25035), let's consider rowID as PK and rename it to shipID
*/
ALTER TABLE globalsuperstore.ship 
RENAME COLUMN rowID TO shipID;

SELECT orderID, COUNT(*) AS cnt
FROM globalsuperstore.ship 
GROUP BY orderID
HAVING count(*) > 1
ORDER BY cnt DESC;
SELECT * 
FROM globalsuperstore.ship
WHERE orderID IN ('CA-2014-100111', 'IN-2013-42311', 'MX-2014-166541', 'IN-2012-41261', 'NI-2014-8880', 'TO-2014-9950')
ORDER BY orderID;

SELECT orderID, count(distinct(shipdate)) AS cnt
FROM globalsuperstore.ship 
GROUP BY orderID
HAVING count(*) > 1
ORDER BY cnt DESC;

SELECT *
FROM globalsuperstore.ship 
where orderID = 'IT-2014-1036058';

SELECT City, State, Country, COUNT(distinct(Market)) -- , COUNT(distinct(Region)), COUNT(distinct(orderID))
FROM globalsuperstore.ship 
GROUP BY City, State, Country
ORDER BY COUNT(distinct(Market)) DESC; -- , COUNT(distinct(Region)), COUNT(distinct(orderID))

SELECT * 
FROM globalsuperstore.ship
WHERE City in (SELECT City-- , COUNT(distinct(Region)), COUNT(distinct(orderID))
FROM globalsuperstore.ship 
GROUP BY City, State, Country
HAVING COUNT(distinct(Market)) > 1) AND
State in (SELECT State-- , COUNT(distinct(Region)), COUNT(distinct(orderID))
FROM globalsuperstore.ship 
GROUP BY City, State, Country
HAVING COUNT(distinct(Market)) > 1) AND
Country in (SELECT Country-- , COUNT(distinct(Region)), COUNT(distinct(orderID))
FROM globalsuperstore.ship 
GROUP BY City, State, Country
HAVING COUNT(distinct(Market)) > 1)
ORDER BY City, State, Country;


SELECT City, State, Country, COUNT(distinct(Region)) -- , COUNT(distinct(Region)), COUNT(distinct(orderID))
FROM globalsuperstore.ship 
GROUP BY City, State, Country
ORDER BY COUNT(distinct(Market)) DESC; -- , COUNT(distinct(Region)), COUNT(distinct(orderID))

SELECT * 
FROM globalsuperstore.ship
WHERE City in (SELECT City-- , COUNT(distinct(Region)), COUNT(distinct(orderID))
FROM globalsuperstore.ship 
GROUP BY City, State, Country
HAVING COUNT(distinct(Region)) > 1) AND
State in (SELECT State-- , COUNT(distinct(Region)), COUNT(distinct(orderID))
FROM globalsuperstore.ship 
GROUP BY City, State, Country
HAVING COUNT(distinct(Region)) > 1) AND
Country in (SELECT Country-- , COUNT(distinct(Region)), COUNT(distinct(orderID))
FROM globalsuperstore.ship 
GROUP BY City, State, Country
HAVING COUNT(distinct(Region)) > 1)
ORDER BY City, State, Country;

SELECT * FROM ship limit 1;
SELECT City, State, COUNT(distinct(Country)) -- , COUNT(distinct(Region)), COUNT(distinct(orderID))
FROM globalsuperstore.ship 
GROUP BY City, State
ORDER BY COUNT(distinct(Country)) DESC; -- , COUNT(distinct(Region)), COUNT(distinct(orderID))

SELECT City, State, COUNT(distinct(Market)) -- , COUNT(distinct(Region)), COUNT(distinct(orderID))
FROM globalsuperstore.ship 
GROUP BY City, State
ORDER BY COUNT(distinct(Market)) DESC; -- , COUNT(distinct(Region)), COUNT(distinct(orderID))

SELECT City, State, COUNT(distinct(postalCode)) -- , COUNT(distinct(Region)), COUNT(distinct(orderID))
FROM globalsuperstore.ship 
GROUP BY City, State
ORDER BY COUNT(distinct(postalCode)) DESC; -- , COUNT(distinct(Region)), COUNT(distinct(orderID))

SELECT orderID, count(*) from orders GROUP BY orderID HAVING count(*) > 1 limit 5;

SELECT * FROM orders 
WHERE orderID in ('IN-2013-77878', 'IN-2013-71249', 'IN-2013-42360', 'IN-2011-81826', 'CA-2012-124891')
ORDER BY orderID;

SELECT prodID, count(*) FROM prod GROUP BY prodID HAVING count(*) > 1 ORDER BY count(*) desc;
SELECT * FROM prod where prodID = 'OFF-AR-10003651';

SELECT prodID, count(Distinct(SubCategory)) FROM prod GROUP BY prodID HAVING count(Distinct(SubCategory)) > 1 ORDER BY count(*) desc;
SELECT * FROM prod where prodID = 'OFF-AVE-10002102'; -- exceptional case; 1 for binder and 1 for folder label
SELECT prodID, count(Distinct(prodName)) FROM prod GROUP BY prodID HAVING count(Distinct(prodName)) > 1 ORDER BY count(*) desc;
SELECT * FROM prod where prodID in ('OFF-AR-10003651', 'OFF-AR-10003829', 'OFF-BI-10002799') order by prodID;

SELECT * from cust limit 3;
SELECT custID, count(distinct(custName)) FROM cust GROUP BY custID HAVING count(distinct(custName)) > 1; 
SELECT custID, count(distinct(Segment)) FROM cust GROUP BY custID HAVING count(distinct(custName)) > 1; 


/*
ALTER TABLE globalsuperstore.ship 
DROP COLUMN orderID;
*/

