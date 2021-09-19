DROP TABLE IF EXISTS ServiceFee;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Request;
DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS Administrator;
DROP TABLE IF EXISTS Customer;


CREATE TABLE Administrator(
	adminID			INT 	        NOT NULL AUTO_INCREMENT,
    adminName 		VARCHAR(255)	NOT NULL,
    adminPassword	VARCHAR(255) 	NOT NULL,
    phoneNumber		VARCHAR(20) 	NOT NULL,
    gender			VARCHAR(20)		NOT NULL,
    PRIMARY KEY (adminID)
);

CREATE TABLE Customer(
	custID			INT          	NOT NULL AUTO_INCREMENT,
    custName 		VARCHAR(255)	NOT NULL,
    custPassword	VARCHAR(255) 	NOT NULL,
    phoneNumber		VARCHAR(20) 	NOT NULL,
    gender			VARCHAR(20)		NOT NULL,
    address			VARCHAR(255) 	NOT NULL,
    email			VARCHAR(255) 	NOT NULL,
    PRIMARY KEY (custID)
);
    
CREATE TABLE Item(
	itemID			INT         	NOT NULL,
    adminID			INT         	,
    purchaseStatus	VARCHAR(255)	NOT NULL,
    serviceStatus	VARCHAR(255)	NOT NULL,
    PRIMARY KEY (itemID),
    FOREIGN KEY (adminID) REFERENCES Administrator(adminID)
);

CREATE TABLE Request(
    requestID       INT             NOT NULL AUTO_INCREMENT,
    requestDate     DATE            NOT NULL,
    requestStatus   VARCHAR(255)    NOT NULL,
    custID      	INT             NOT NULL,
    adminID         INT             NOT NULL,
    itemID          INT             NOT NULL,
    PRIMARY KEY (requestID),
    FOREIGN KEY (custID) REFERENCES Customer(custID),
    FOREIGN KEY (adminID) REFERENCES Administrator(adminID),
    FOREIGN KEY (itemID) REFERENCES Item(itemID)
);

CREATE TABLE Payment(
    paymentID		INT          	NOT NULL AUTO_INCREMENT,
    custID			INT          	NOT NULL,
    requestID		INT          	NOT NULL,
    paymentDate     DATE            NOT NULL,
    paymentAmount   DECIMAL(10,2)   NOT NULL	CHECK (paymentAmount >= 0),
    PRIMARY KEY (paymentID),
    FOREIGN KEY (custID) REFERENCES Customer(custID),
    FOREIGN KEY (requestID) REFERENCES Request(requestID)
);

CREATE TABLE ServiceFee(
    requestID       INT             NOT NULL,
    creationDate    DATE            NOT NULL,
    feeAmount       DECIMAL(10,2)   NOT NULL	CHECK (feeAmount >= 0),
    FOREIGN KEY (requestID) REFERENCES Request(requestID)
);

INSERT INTO Administrator (
    addressasdf
    addressfasdf

)