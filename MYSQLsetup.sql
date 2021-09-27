
SET GLOBAL FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS ServiceFee;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Request;
DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Administrator;
DROP TABLE IF EXISTS Customer;

CREATE TABLE Administrator(
	adminID			    INT 	        NOT NULL    AUTO_INCREMENT,
    adminName 		    VARCHAR(255)	NOT NULL,
    adminPassword	    VARCHAR(255) 	NOT NULL,
    phoneNumber		    VARCHAR(20) 	NOT NULL,
    gender			    VARCHAR(20)		NOT NULL,
    PRIMARY KEY (adminID)
);

CREATE TABLE Customer(
	customerID			INT          	NOT NULL    AUTO_INCREMENT,
    customerName 		VARCHAR(255)	NOT NULL,
    customerPassword	VARCHAR(255) 	NOT NULL,
    phoneNumber		    VARCHAR(20) 	NOT NULL,
    gender			    VARCHAR(20)		NOT NULL,
    address			    VARCHAR(255) 	NOT NULL,
    email			    VARCHAR(255) 	NOT NULL,
    PRIMARY KEY (customerID)
);

CREATE TABLE Product(
    productID           INT             NOT NULL,
    warrantyDuration    INT             NOT NULL,
    PRIMARY KEY (productID)
);

CREATE TABLE Item(
	itemID			    INT         	NOT NULL,
    productID           INT             NOT NULL,
    adminID			    INT         	,           -- NULL if no service request 
    customerID			INT         	,           -- NULL if not purchased
    purchaseStatus	    VARCHAR(255)	NOT NULL,
    serviceStatus	    VARCHAR(255)	NOT NULL,
    dateOfPurchase      DATE            ,           -- NULL if not purchased
    PRIMARY KEY (itemID),
    FOREIGN KEY (productID) REFERENCES Product(productID),
    FOREIGN KEY (adminID) REFERENCES Administrator(adminID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID)
);

CREATE TABLE Request(
    requestID           INT             NOT NULL    AUTO_INCREMENT,
    requestDate         DATE            NOT NULL,
    requestStatus       VARCHAR(255)    NOT NULL,
    customerID      	INT             NOT NULL,
    adminID             INT             ,
    itemID              INT             NOT NULL,
    PRIMARY KEY (requestID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID),
    FOREIGN KEY (adminID) REFERENCES Administrator(adminID),
    FOREIGN KEY (itemID) REFERENCES Item(itemID)
);

CREATE TABLE Payment(
    paymentID		    INT          	NOT NULL    AUTO_INCREMENT,
    customerID			INT          	NOT NULL,
    requestID		    INT          	NOT NULL,
    paymentDate         DATE            NOT NULL,
    paymentAmount       DECIMAL(10,2)   NOT NULL	CHECK (paymentAmount >= 0),
    PRIMARY KEY (paymentID),
    FOREIGN KEY (customerID) REFERENCES Customer(customerID),
    FOREIGN KEY (requestID) REFERENCES Request(requestID)
);

CREATE TABLE ServiceFee(
    requestID           INT             NOT NULL,
    creationDate        DATE            NOT NULL,
    feeAmount           DECIMAL(10,2)   NOT NULL	CHECK (feeAmount >= 0),
    FOREIGN KEY (requestID) REFERENCES Request(requestID)
);