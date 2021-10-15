drop database oshes;
CREATE DATABASE OSHES;
USE OSHES;
CREATE TABLE Customer(
    customerID 	VARCHAR(15) NOT NULL,
    name 		VARCHAR(30) NOT NULL,
    gender 		CHAR NOT NULL CHECK (Gender IN ('M', 'F')),
    email 		VARCHAR(30) NOT NULL,
    phoneNumber VARCHAR(15) NOT NULL,
    address 	VARCHAR(150) NOT NULL,
    password 	VARCHAR(30) NOT NULL,
    PRIMARY KEY (CustomerID));
    
CREATE TABLE Administrator(
    administratorID 	VARCHAR(15) NOT NULL,
    name 				VARCHAR(30) NOT NULL,
    gender 				CHAR NOT NULL CHECK (Gender IN ('M', 'F')),
    phoneNumber 		VARCHAR(15) NOT NULL,
    password			VARCHAR(30) NOT NULL,
    PRIMARY KEY (AdministratorID));
    
INSERT INTO Administrator VALUES ("master", "Kevin", "M", "82437123", "admin"); 