import mysql.connector


class MySQLInitialization:

    def initialize_database(self):

        con = mysql.connector.connect(host="localhost",
                                                 database="oshes",
                                                 user="root",
                                                 password="sxbl15302")

        cur1 = con.cursor()
        cur1.execute("CREATE TABLE Product( productID VARCHAR(15) NOT NULL," +
                                              "productModel VARCHAR(10) NOT NULL," +
                                              "category VARCHAR(6) NOT NULL," +
                                              "price VARCHAR(30) NOT NULL," +
                                              "warrantyDuration VARCHAR(30) NOT NULL," +
                                              "PRIMARY KEY(productID))")
        cur2 = con.cursor()
        cur2.execute("CREATE TABLE Item(" +
                                              "itemID VARCHAR(15) NOT NULL," +
                                              "purchaseStatus VARCHAR(6) NOT NULL " +
                                              "CHECK (purchaseStatus IN ('Unsold', 'Sold'))," +
                                              "factory VARCHAR(30)," +
                                              "producationYear VARCHAR(4)," +
                                              "color VARCHAR(15)," +
                                              "powerSupply VARCHAR(30)," +
                                              "serviceStatus VARCHAR(20) DEFAULT NULL " +
                                              "CHECK (serviceStatus IN (NULL, 'Waiting for approval', 'In progress', 'Completed'))," +
                                              "administratorID VARCHAR(15) DEFAULT NULL," +
                                              "productID VARCHAR(15) DEFAULT NULL," +
                                              "customerID VARCHAR(15) DEFAULT NULL," +
                                              "dateOfPurchase DATE DEFAULT NULL," +
                                              "PRIMARY KEY(itemID)," +
                                              "FOREIGN KEY(administratorID) REFERENCES Administrator(administratorID)," +
                                              "FOREIGN KEY(productID) REFERENCES Product(productID)," +
                                              "FOREIGN KEY(customerID) REFERENCES Customer(customerID))")

        cur3 = con.cursor()
        cur3.execute("CREATE TABLE Request(" +
                                              "requestID VARCHAR(15) NOT NULL," +
                                              "requestStatus VARCHAR(50) NOT NULL CHECK (requestStatus IN (NULL, 'Submitted', 'Submitted and Waiting for payment','In progress','Approved', 'Canceled','Completed'))," +
                                              "requestDate DATE," +
                                              "customerID VARCHAR(15) NOT NULL," +
                                              "administratorID  VARCHAR(15)," +
                                              "itemID VARCHAR(15) NOT NULL," +
                                              "PRIMARY KEY (requestID)," +
                                              "FOREIGN KEY (customerID) REFERENCES Customer(customerID)," +
                                              "FOREIGN KEY (administratorID) REFERENCES Administrator(administratorID)," +
                                              "FOREIGN KEY (itemID) REFERENCES Item(itemID))")

        cur4 = con.cursor()
        cur4.execute("CREATE TABLE Payment(" +
                                              "paymentID VARCHAR(15) NOT NULL," +
                                              "paymentDate DATE," +
                                              "paymentAmt SMALLINT," +
                                              "customerID VARCHAR(15) NOT NULL," +
                                              "PRIMARY KEY (paymentID)," +
                                              "FOREIGN KEY (customerID) REFERENCES Customer(customerID))")

        cur5 = con.cursor()
        cur5.execute("CREATE TABLE ServiceFee(" +
                                              "requestID VARCHAR(30) NOT NULL," +
                                              "paymentID VARCHAR(30) NOT NULL," +
                                              "creationDate DATE," +
                                              "flatFee SMALLINT," +
                                              "materialFee SMALLINT," +
                                              "PRIMARY KEY (requestID, PaymentID, creationDate))")

        con.close()

main = MySQLInitialization()
main.initialize_database()


