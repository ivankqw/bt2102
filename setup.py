import mysql.connector
from mysql.connector.errors import OperationalError
from pymongo import MongoClient
from pymongo import TEXT
import json
import pandas as pd
from sqlalchemy import create_engine

# Create MYSQL Database
def create_db_mysql(host='localhost',user='root',password=''):
    mydb = mysql.connector.connect(host=host,user=user,passwd=password)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE oshes")
    mydb.close()

# Create MongoDB Database
def init_mongo():
    client = MongoClient()
    mongo = client['Inventory']
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
    mongo = client['Inventory']
    items = mongo.items
    products = mongo.products
    items.drop_indexes()
    items.create_index([("Category", TEXT), ("Model", TEXT)])
    return

# MYSQL Schema
def init_mysql(host='localhost',user='root',password=''):
    mydb = mysql.connector.connect(host=host,user=user,passwd=password,database="oshes")
    mycursor = mydb.cursor()
    
    with open('MYSQLSetup.sql', 'r') as SQLscript:
        SQLcommands = SQLscript.read().split(';')
        for command in SQLcommands:
            mycursor.execute(command)
            
    mydb.close()

# Items.json info to MYSQL, while taking ProductID from products.json
def items_info_to_sql(password):
    # def getProductIdOfItem(category, model):
    #     client = MongoClient()
    #     mongo = client['Inventory']
    #     products = mongo.products
    #     return list(products.find({'Category': category, 'Model' : model}))[0]['ProductID']
    def getProductID(category, model):
        p = open('products.json')
        p = json.load(p)
        for i in p:
            if i['Category'] == category and i['Model'] == model:
                return i['ProductID']
    items_df = pd.read_json('items.json')
    items_df['productID'] = items_df.apply(lambda row : getProductID(row.Category, row.Model), axis=1)
    items_sql_df = items_df[["ItemID", "PurchaseStatus", "ServiceStatus", "productID"]]
    
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                        .format(user="root",
                                pw=password,
                                db="oshes"))

    items_sql_df.to_sql('item', con = engine, if_exists='append', index=False)

# products.json info to MYSQL
def products_info_to_sql(password):
    products_df = pd.read_json('products.json')
    products_sql_df = products_df[["ProductID", "Warranty (months)"]]
    products_sql_df.rename({"Warranty (months)": 'warrantyDuration'}, axis=1, inplace=True)
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                        .format(user="root",
                                pw=password,
                                db="oshes"))

    products_sql_df.to_sql('product', con = engine, if_exists='append', index=False)

#fake data for request -> payment testing purposes
def init_fake(host='localhost',user='root',password=''):
    mydb = mysql.connector.connect(host=host,user=user,passwd=password,database="oshes")
    mycursor = mydb.cursor()
    
    with open('FakeItemData.sql', 'r') as SQLscript:
        SQLcommands = SQLscript.read().split(';')
        for command in SQLcommands:
            mycursor.execute(command)
            
    mydb.close()

#create_db_mysql(password='')

'''run these'''
# init_mysql(password="Valentin1")
# items_info_to_sql(password="Valentin1")
# products_info_to_sql(password="Valentin1")
# init_fake(password="Valentin1")


