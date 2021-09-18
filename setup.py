from pymongo import MongoClient
from pymongo import TEXT
import json
import pandas as pd
from sqlalchemy import create_engine

def init_mongo():
    client = MongoClient()
    mongo = client['testdb']
    items = mongo.items
    products = mongo.products
    with open('items.json') as i:
        i_data = json.load(i)
    with open('products.json') as p:
        p_data = json.load(p)
    
    items.insert_many(i_data)
    products.insert_many(p_data)

def create_indexes_mongo():
    #simple search
    client = MongoClient()
    mongo = client['testdb']
    items = mongo.items
    products = mongo.products
    items.drop_indexes()
    items.create_index([("Category", TEXT), ("Model", TEXT)])
    return

def init_mysql():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="oshes"
    )
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS ServiceFee")
    mycursor.execute("DROP TABLE IF EXISTS Payment")
    mycursor.execute("DROP TABLE IF EXISTS Request")
    mycursor.execute("DROP TABLE IF EXISTS Item")
    mycursor.execute("DROP TABLE IF EXISTS Administrator")
    mycursor.execute("DROP TABLE IF EXISTS Customer")
    
    mycursor.execute("CREATE TABLE Administrator (adminID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), password VARCHAR(255), phoneNumber VARCHAR(255), gender VARCHAR(255))")
    mycursor.execute("CREATE TABLE Customer (customerID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), password VARCHAR(255), phoneNumber VARCHAR(255), gender VARCHAR(255), address VARCHAR(255), email VARCHAR(255))")
    mycursor.execute("CREATE TABLE Item (itemID INT AUTO_INCREMENT PRIMARY KEY, adminID INT, purchaseStatus VARCHAR(255), serviceStatus VARCHAR(255))")
    mycursor.execute("CREATE TABLE Payment (paymentID INT AUTO_INCREMENT PRIMARY KEY, customerID INT, requestID INT, paymentDate DATE)")
    mycursor.execute("CREATE TABLE Request (requestID INT AUTO_INCREMENT PRIMARY KEY, customerID INT, adminID INT, itemID INT, requestDate DATE, requestStatus VARCHAR(255))")
    mycursor.execute("CREATE TABLE ServiceFee (requestID INT PRIMARY KEY, creationDate DATE, feeAmount DOUBLE)")
    mycursor.execute("ALTER TABLE ServiceFee ADD FOREIGN KEY(requestID) references Request(requestID)")
    mycursor.execute("ALTER TABLE Request ADD FOREIGN KEY(customerID) references Customer(customerID)")
    mycursor.execute("ALTER TABLE Request ADD FOREIGN KEY(adminID) references Administrator(adminID)")
    mycursor.execute("ALTER TABLE Request ADD FOREIGN KEY(itemID) references Item(itemID)")
    mycursor.execute("ALTER TABLE Payment ADD FOREIGN KEY(customerID) references Customer(customerID)")
    mycursor.execute("ALTER TABLE Payment ADD FOREIGN KEY(requestID) references Request(requestID)")
    mycursor.execute("ALTER TABLE Item ADD FOREIGN KEY(adminID) references Administrator(adminID)")
    mydb.close()

def items_info_to_sql():
    items_df = pd.read_json('items.json')
    items_sql_df = items_df[["ItemID", "PurchaseStatus", "ServiceStatus"]]
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                        .format(user="root",
                                pw="root",
                                db="oshes"))

    items_sql_df.to_sql('item', con = engine, if_exists='append', index=False)