/* 
README
----------
2026-02-05 12:19:
Recreate the tables after prelim exploring, old script is archieved and stored in another folder.  
SELECT prodID, count(distinct(prodName)) FROM globalSuperStore.prod GROUP BY prodID HAVING count(distinct(prodName)) > 1;
show 457 in 10292 of supposed PK prodID has more than 1 prodName 
Surprisingly orderID cannot be sufficent PK for order table; instead it could have multiply orderDate and orderPriority
Therefore need to be merging order and ship into 1 (say order)
2026-02-5 16:20:
4 tables are created; 
table 'cust' has PK 'custID'  
table 'orders' has PK 'uniqueID' and 1) FK 'custID' to Table 'cust' 2) FK 'uniqueID' to table 'ship_prod'
table 'ship_prod' has PK 'uniqueID'  
table 'prod' has PK 'prodID' (also exluding prodID = 'OFF-AVE-10002102') 
51278 count for the new tables consider 51290
This would be a model that can store most of data in the raw dataset, 
but not ideal relations schema for the global super store. 
Will use the datatype of raw dataset to redesign
*/
DROP TABLE globalSuperStore.cust;
DROP TABLE globalSuperStore.orders;
DROP TABLE globalSuperStore.prod;
DROP TABLE globalsuperstore.prod_2;
DROP TABLE globalsuperstore.ship_prod;
DROP TABLE globalSuperStore.ship;
DROP TABLE check_table;
DROP TABLE orders_raw.orders;
DROP DATABASE orders_raw;
DROP DATABASE globalSuperStore;
CREATE DATABASE Orders_raw;
USE Orders_raw;
SET GLOBAL local_infile = 1;

-- TABLE DATA IMPORT 

TRUNCATE TABLE orders_raw.orders;
SELECT * FROM orders_raw.orders;
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
SET GLOBAL local_infile = 0;

DESCRIBE orders_raw.orders;
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
CHANGE COLUMN `Row ID` `shipID` INT NOT NULL ,
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

CREATE DATABASE globalSuperStore;
USE globalSuperStore;

CREATE TABLE globalSuperStore.cust AS
SELECT DISTINCT custID, custName, Segment
FROM orders_raw.orders;

SELECT count(*) FROM globalSuperStore.cust;  -- 1590 count for table 'cust'

-- SELECT prodID, count(distinct(prodName)) FROM globalSuperStore.prod GROUP BY prodID HAVING count(distinct(prodName)) > 1;
-- SELECT count(distinct(prodID)) FROM globalSuperStore.prod; 457 in 10292,
CREATE TABLE globalSuperStore.prod AS
SELECT DISTINCT prodID, Category, SubCategory
FROM orders_raw.orders; -- 10293

/*
CREATE TABLE globalSuperStore.orders AS
SELECT DISTINCT orderID, orderDate, orderPriority
FROM orders_raw.orders; -- 25753

-- 38 orderID and prodID not enough jointly,  
SELECT orderID, prodID, count(*) FROM orders_raw.orders GROUP BY orderID, prodID HAVING count(*) > 1; 
*/
SELECT *
FROM (
    SELECT *,
           COUNT(*) OVER(PARTITION BY orderID, prodID) as occurrence_count
    FROM orders_raw.orders
) t
WHERE occurrence_count > 1
ORDER BY orderID, prodID; -- 76 counts
-- SELECT * FROM orders_raw.orders WHERE orderID = 'AG-2014-4840' and prodID = 'TEC-MEM-10002524';

CREATE TABLE globalSuperStore.ship_prod AS
SELECT shipID, shipDate, prodID, prodName, Profit, Discount, Quantity, Sales
FROM orders_raw.orders;

/*
CREATE TABLE globalSuperStore.ship AS
SELECT shipID, shipMode, ShippingCost, City, State, Country, postalCode, Market, Region 
FROM orders_raw.orders;

SELECT orderID, count(*) FROM globalSuperStore.orders GROUP BY orderID having count(*) > 1 ORDER BY count(*) DESC; # order ID still not unique
-- 660 of order ID has multi count
SELECT * FROM orders WHERE orderID = 'ES-2014-4717877';

SELECT * FROM globalSuperStore.orders WHERE orderID = 'ES-2014-4717877';
SELECT * FROM orders_raw.orders WHERE orderID = 'ES-2014-4717877';
DROP TABLE IF EXISTS globalSuperStore.orders;
DROP TABLE IF EXISTS globalSuperStore.ship;
*/
CREATE TABLE globalSuperStore.orders AS
SELECT DISTINCT orderID, orderDate, orderPriority, shipID, custID, shipMode, ShippingCost, City, State, Country, postalCode, Market, Region 
FROM orders_raw.orders;

ALTER TABLE globalsuperstore.orders 
RENAME COLUMN shipID TO uniqueID;

ALTER TABLE globalsuperstore.ship_prod 
RENAME COLUMN shipID TO uniqueID;

-- adding PK and then FK in tables
ALTER TABLE cust
ADD PRIMARY KEY (custID);
ALTER TABLE orders
ADD PRIMARY KEY (uniqueID);
-- ALTER TABLE prod
-- ADD PRIMARY KEY (prodID);
SET SQL_SAFE_UPDATES = 0;
DELETE FROM prod
WHERE prodID = 'OFF-AVE-10002102';
SET SQL_SAFE_UPDATES = 1;

SELECT * FROM prod limit 1;
SELECT prodID, Category, count(SubCategory) FROM prod GROUP BY prodID, Category HAVING count(SubCategory) > 1 ORDER BY prodID;
-- SELECT * FROM prod WHERE prodID = 'FUR-ADV-10000183';

/*
CREATE TABLE globalSuperStore.prod_2 AS
SELECT DISTINCT *
FROM globalSuperStore.prod;
*/
ALTER TABLE prod
ADD PRIMARY KEY (prodID);
 
-- DROP TABLE IF EXISTS globalSuperStore.prod;

SELECT * FROM cust limit 1;
SELECT * FROM orders limit 1;
SELECT * FROM prod limit 1;
SELECT * FROM ship_prod limit 1;
SELECT count(*) from ship_prod limit 1; -- 51290
SELECT count(*) from cust limit 1; -- 1590
SELECT count(*) from orders limit 1; -- 51290
SELECT count(*) from prod limit 1; -- 10291
DESC ship_prod;
DESC cust;
DESC orders;
DESC prod;

ALTER TABLE ship_prod
ADD PRIMARY KEY (uniqueID);

SELECT custID, count(*) FROM cust group by custID having count(*) > 1;

CREATE TABLE check_table AS
SELECT orders.orderID, orders.orderDate, orders.orderPriority, orders.uniqueID, orders.shipMode,
orders.ShippingCost, orders.City, orders.State, orders.Country, orders.postalCode, orders.Market, orders.Region,
ship_prod.prodName, ship_prod.Discount, ship_prod.Profit, ship_prod.Quantity, ship_prod.Sales, ship_prod.prodID, 
ship_prod.shipDate, prod.Category, prod.SubCategory, orders.custID, cust.custName, cust.Segment
FROM orders
INNER JOIN ship_prod
ON orders.uniqueID = ship_prod.uniqueID
INNER JOIN cust
ON orders.custID = cust.custID
INNER JOIN prod
ON ship_prod.prodID = prod.prodID; -- 51278 count

DESC check_table;
DESC orders_raw.orders;