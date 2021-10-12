CREATE DATABASE OSHES;
USE OSHES;
CREATE TABLE Customer(
    customerID VARCHAR(15) NOT NULL,
    name VARCHAR(30) NOT NULL,
    gender CHAR NOT NULL CHECK (Gender IN ('M', 'F')),
    email VARCHAR(30) NOT NULL,
    phoneNumber VARCHAR(15) NOT NULL,
    address VARCHAR(150) NOT NULL,
    password VARCHAR(30) NOT NULL,
    PRIMARY KEY (CustomerID));
    
CREATE TABLE Administrator(
    administratorID VARCHAR(15) NOT NULL,
    name VARCHAR(30) NOT NULL,
    gender CHAR NOT NULL CHECK (Gender IN ('M', 'F')),
    phoneNumber VARCHAR(15) NOT NULL,
    password VARCHAR(30) NOT NULL,
    PRIMARY KEY (AdministratorID));

CREATE TABLE Product(
    productID VARCHAR(15) NOT NULL,
    productModel VARCHAR(10) NOT NULL,
    category VARCHAR(6) NOT NULL,
    price VARCHAR(30) NOT NULL,
    cost VARCHAR(30) NOT NULL,
    warrantyDuration VARCHAR(30) NOT NULL,
    PRIMARY KEY(productID));

CREATE TABLE Item(
    itemID VARCHAR(15) NOT NULL,
    purchaseStatus VARCHAR(6) NOT NULL
    CHECK (purchaseStatus IN ('Unsold', 'Sold')),
    factory VARCHAR(30),
    producationYear VARCHAR(4),
    color VARCHAR(15),
    powerSupply VARCHAR(30),
    serviceStatus VARCHAR(20) DEFAULT NULL
    CHECK (serviceStatus IN (NULL, 'Waiting for approval', 'In progress', 'Completed')),
    administratorID VARCHAR(15) DEFAULT NULL,
    productID VARCHAR(15) DEFAULT NULL,
    customerID VARCHAR(15) DEFAULT NULL,
    dateOfPurchase DATE DEFAULT NULL,
    PRIMARY KEY(itemID),
    FOREIGN KEY(administratorID) REFERENCES Administrator(administratorID),
    FOREIGN KEY(productID) REFERENCES Product(productID),
    FOREIGN KEY(customerID) REFERENCES Customer(customerID));

CREATE TABLE Request(
    requestID VARCHAR(15) NOT NULL,
    requestStatus VARCHAR(50) IN (NULL,'Submitted',
                   'Submitted and Waiting for payment','In progress','Approved',
                   'Canceled','Completed')),
    requestDate DATE, 
    customerID VARCHAR(15) NOT NULL,
    administratorID  VARCHAR(15),
    itemID VARCHAR(15) NOT NULL,
    PRIMARY KEY (requestID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID),
    FOREIGN KEY (administratorID) REFERENCES Administrator(administratorID),
    FOREIGN KEY (itemID) REFERENCES Item(itemID));

CREATE TABLE Payment(
    paymentID VARCHAR(15) NOT NULL,
    paymentDate DATE,
    paymentAmt SMALLINT, 
    customerID VARCHAR(15) NOT NULL,
    PRIMARY KEY (paymentID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID));

CREATE TABLE ServiceFee(
    requestID VARCHAR(30) NOT NULL,
    paymentID VARCHAR(30) NOT NULL,
    creationDate DATE,
    flatFee SMALLINT, 
    materialFee SMALLINT,
    PRIMARY KEY (requestID, PaymentID, creationDate));

