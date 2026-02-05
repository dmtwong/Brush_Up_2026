CREATE SCHEMA IF NOT EXISTS gss_warehouse DEFAULT CHARACTER SET utf8;
USE gss_warehouse;

-- Dimension tables
CREATE TABLE dim_product (
  prodID VARCHAR(30) NOT NULL,
  prodName VARCHAR(150) NOT NULL,
  Category VARCHAR(25) NOT NULL,
  SubCategory VARCHAR(25) NOT NULL,
  PRIMARY KEY (prodID)
);

CREATE TABLE dim_location (
  addressID INT NOT NULL,
  City VARCHAR(50) NOT NULL,
  State VARCHAR(50) NULL,
  Country VARCHAR(50) NOT NULL,
  Market VARCHAR(10) NOT NULL,
  Region VARCHAR(20) NOT NULL,
  postalCode VARCHAR(10) NULL,
  PRIMARY KEY (addressID)
);

CREATE TABLE dim_time (
  date_key DATE NOT NULL,
  year INT NOT NULL,
  quarter INT NOT NULL,
  month INT NOT NULL,
  day INT NOT NULL,
  day_name VARCHAR(10),
  is_weekend BOOLEAN,
  PRIMARY KEY (date_key)
);

-- fact table
CREATE TABLE fact_sales (
  salesID INT NOT NULL AUTO_INCREMENT,
  orderID VARCHAR(16) NOT NULL,
  custID VARCHAR(9) NOT NULL,
  prodID VARCHAR(30) NOT NULL,
  addressID INT NOT NULL,
  order_date_key DATE NOT NULL,
  Quantity INT NOT NULL,
  Sale DOUBLE NOT NULL,
  Discount DOUBLE NOT NULL,
  Profit DOUBLE NOT NULL,
  ShippingCost DOUBLE NOT NULL,
  PRIMARY KEY (salesID),
  FOREIGN KEY (prodID) REFERENCES dim_product(prodID),
  FOREIGN KEY (addressID) REFERENCES dim_location(addressID),
  FOREIGN KEY (order_date_key) REFERENCES dim_time(date_key)
);