-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema revised_gss
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema revised_gss
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `revised_gss` DEFAULT CHARACTER SET utf8 ;
USE `revised_gss` ;

-- -----------------------------------------------------
-- Table `revised_gss`.`cust`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `revised_gss`.`cust` (
  `custID` VARCHAR(9) NOT NULL,
  `custName` VARCHAR(50) NOT NULL,
  `Segment` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`custID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `revised_gss`.`prod`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `revised_gss`.`prod` (
  `prodID` VARCHAR(30) NOT NULL,
  `prodName` VARCHAR(150) NOT NULL,
  `Category` VARCHAR(25) NOT NULL,
  `SubCategory` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`prodID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `revised_gss`.`address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `revised_gss`.`address` (
  `addressID` INT NOT NULL AUTO_INCREMENT,
  `City` VARCHAR(50) NOT NULL,
  `State` VARCHAR(50) NULL,
  `Country` VARCHAR(50) NOT NULL,
  `Market` VARCHAR(10) NOT NULL,
  `Region` VARCHAR(20) NOT NULL,
  `postalCode` VARCHAR(10) NULL,
  PRIMARY KEY (`addressID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `revised_gss`.`ship`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `revised_gss`.`ship` (
  `shipID` INT NOT NULL,
  `addressID` INT NOT NULL,
  `shipDate` DATE NOT NULL,
  `shipMode` VARCHAR(30) NOT NULL,
  `ShippingCost` DOUBLE NOT NULL,
  PRIMARY KEY (`shipID`),
  INDEX `fk_ship_address_idx` (`addressID` ASC) VISIBLE,
  CONSTRAINT `fk_ship_address`
    FOREIGN KEY (`addressID`)
    REFERENCES `revised_gss`.`address` (`addressID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `revised_gss`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `revised_gss`.`orders` (
  `orderID` VARCHAR(16) NOT NULL,
  `custID` VARCHAR(9) NOT NULL,
  `prodID` VARCHAR(30) NOT NULL,
  `shipID` INT NOT NULL,
  `Quantity` INT NOT NULL,
  `Sale` DOUBLE NOT NULL,
  `orderPriority` VARCHAR(15) NOT NULL,
  `Discount` DOUBLE NOT NULL,
  `Profit` DOUBLE NOT NULL,
  `orderDate` DATE NOT NULL,
  PRIMARY KEY (`orderID`),
  INDEX `fk_orders_cust_idx` (`custID` ASC) VISIBLE,
  INDEX `fk_orders_prod_idx` (`prodID` ASC) VISIBLE,
  INDEX `fk_orders_ship_idx` (`shipID` ASC) VISIBLE,
  CONSTRAINT `fk_orders_cust`
    FOREIGN KEY (`custID`)
    REFERENCES `revised_gss`.`cust` (`custID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_orders_prod`
    FOREIGN KEY (`prodID`)
    REFERENCES `revised_gss`.`prod` (`prodID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_orders_ship`
    FOREIGN KEY (`shipID`)
    REFERENCES `revised_gss`.`ship` (`shipID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
