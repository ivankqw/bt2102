import mysql.connector
from mysql.connector.errors import OperationalError
from pymongo import MongoClient
from pymongo import TEXT
import json
import pandas as pd
from sqlalchemy import create_engine

def create_db_mysql(host='localhost',user='root',password=''):
    mydb = mysql.connector.connect(host=host,user=user,passwd=password)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE oshes")
    mydb.close()

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

def init_mysql(host='localhost',user='root',password=''):
    mydb = mysql.connector.connect(host=host,user=user,passwd=password,database="oshes")
    mycursor = mydb.cursor()
    
    with open('MYSQLSetup.sql', 'r') as SQLscript:
        SQLcommands = SQLscript.read().split(';')
        for command in SQLcommands:
            try:
                mycursor.execute(command)
            except:
                pass
    mydb.close()

def items_info_to_sql(password):
    items_df = pd.read_json('items.json')
    items_sql_df = items_df[["ItemID", "PurchaseStatus", "ServiceStatus"]]
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                        .format(user="root",
                                pw=password,
                                db="oshes"))

    items_sql_df.to_sql('item', con = engine, if_exists='append', index=False)



#create_db_mysql(password='s9938580d')
