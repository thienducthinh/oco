DROP DATABASE IF EXISTS OcoMainDB;

CREATE DATABASE OcoMainDB DEFAULT CHARACTER SET = 'utf8mb4';

USE OcoMainDB;

-- Drop existing tables to avoid conflicts
DROP TABLE IF EXISTS City;
DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS Warehouse;
DROP TABLE IF EXISTS supplier_price_book;
DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS Entity;

-- Create the Item table
-- Drop existing tables to avoid conflicts
DROP TABLE IF EXISTS InventoryTransaction;
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Warehouse;
DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS City;
DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS Entity;

-- Create the Entity table
CREATE TABLE Entity (
    entity_id INT(6) ZEROFILL AUTO_INCREMENT PRIMARY KEY,
    entity_name VARCHAR(255) NOT NULL,
    entity_type ENUM('Supplier', 'Distributor', 'Retailer') NOT NULL,
    entity_address VARCHAR(255) NOT NULL,
    entity_phone VARCHAR(15),
    entity_email VARCHAR(100),
    entity_website VARCHAR(100),
    entity_contact_person VARCHAR(100),
    entity_contact_phone VARCHAR(15),
    entity_contact_email VARCHAR(100),
    entity_contact_position VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the Country table
CREATE TABLE Country (
    country_id SMALLINT PRIMARY KEY,
    country VARCHAR(50) NOT NULL,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the Province table
CREATE TABLE Province (
    province_id SMALLINT PRIMARY KEY,
    province VARCHAR(50) NOT NULL,
    country_id SMALLINT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES Country(country_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Create the City table
CREATE TABLE City (
    city_id SMALLINT PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    province_id SMALLINT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (province_id) REFERENCES Province(province_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Create the Address table
CREATE TABLE Address (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    address_line1 VARCHAR(255) NOT NULL,
    address_line2 VARCHAR(255),
    city_id SMALLINT,
    postal_code VARCHAR(20),
    entity_id INT(6) ZEROFILL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (city_id) REFERENCES City(city_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (entity_id) REFERENCES Entity(entity_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
-- Create the Item table
CREATE TABLE Item (
    item_id INT(7) ZEROFILL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the Warehouse table
CREATE TABLE Warehouse (
    warehouse_id INT(8) PRIMARY KEY,
    entity_id INT(6) ZEROFILL NOT NULL,
    warehouse_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (entity_id) REFERENCES Entity(entity_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Create the Inventory table
CREATE TABLE Inventory (
    warehouse_id INT(8),
    item_id INT(7) ZEROFILL,
    quantity INT NOT NULL,
    PRIMARY KEY (warehouse_id, item_id),
    FOREIGN KEY (warehouse_id) REFERENCES Warehouse(warehouse_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (item_id) REFERENCES Item(item_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Create the InventoryTransaction table
CREATE TABLE InventoryTransaction (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    warehouse_id INT(8),
    item_id INT(7) ZEROFILL,
    transaction_type ENUM('IN', 'OUT') NOT NULL,
    quantity INT NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    inventory_after_transaction INT NOT NULL,
    FOREIGN KEY (warehouse_id) REFERENCES Warehouse(warehouse_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (item_id) REFERENCES Item(item_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE supplier_price_book (
    supplier_id INT(6) ZEROFILL,
    item_id INT(7) ZEROFILL,
    price DECIMAL(10, 0),
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (supplier_id, item_id),
    FOREIGN KEY (supplier_id) REFERENCES Entity(entity_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (item_id) REFERENCES Item(item_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO supplier_price_book (supplier_id, item_id, price)
VALUES
(000001, 100001, 10.00),
(000001, 100002, 20.00),
(000001, 100003, 30.00),
(000002, 100001, 15.00),
(000002, 100002, 25.00),
(000002, 100003, 35.00),
(000003, 100001, 12.00),
(000003, 100002, 22.00),
(000003, 100003, 32.00);