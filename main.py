import tkinter
import tkinter.messagebox as messagebox
import mysql.connector
from pymongo import MongoClient
from pymongo import ASCENDING 
from pymongo import DESCENDING 
from pymongo import TEXT
import json
import pprint
import re

client = MongoClient()
mongo = client['testdb']
items = mongo.items
products = mongo.products

def Button(): 
    root = tkinter.Tk() 
    root.geometry('1000x1000')
    btn = tkinter.Button(root, text = "press me i am button", bd = 5, command = root.destroy)
    btn.pack(side = "top")
    root.mainloop()
    
    
def CommonSignUpPage():
    #common attributes: userId, password
    return 

def AdminSignUpPage(): 
    #sign up as an admin 
    ##attributes: adminId, name, gender, phone, password 
    return 

def CustomerSignUpPage(cursor, db):
    #sign up as a customer 
    ##attributes: customerId, name, gender, email, phone, address, password 
    def validate_signup():
        check_counter=0
        warn = ""
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        insert_statement = "INSERT INTO Customer (name, password, phoneNumber, gender, address, email) VALUES (%s, %s, %s, %s, %s, %s)"
        if register_name.get() == "":
            warn += "\n"
            warn += "Name cannot be empty!"
        else:
            check_counter += 1
        check_counter=0
                
        if register_email.get() == "":
            warn += "\n"
            warn += "Email cannot be empty!"
        else:
            check_counter += 1
        if (not re.fullmatch(regex, register_email.get())):
            warn += "\n"
            warn += "Please enter a valid email address!"
        else:
            check_counter += 1
        if register_mobile.get() == "":
            warn += "\n"
            warn += "Phone number cannot be empty!"
        else:
            check_counter += 1
        if ((len(register_mobile.get()) != 8) or (not register_mobile.get().isdigit())):
            print(len(register_mobile.get()))
            warn += "\n"
            warn += "Please enter a valid mobile number! (8 digits)"
        else:
            check_counter += 1 
        if register_address.get() == "":
            warn += "\n"
            warn += "Address cannot be empty!"
        else:
            check_counter += 1        
        if  var.get() == "":
            warn += "\n"        
            warn += "Select Gender"
        else:
            check_counter += 1

        if register_pwd.get() == "":
            warn += "\n"
            warn += "Password cannot be empty!"
        else:
            check_counter += 1

        if pwd_again.get() == "":
            warn += "\n"
            warn += "Re-enter password cannot be empty!"
        else:
            check_counter += 1
        if pwd_again.get() != register_pwd.get():
            warn += "\n"
            warn += "Passwords not matching!"
        else:
            check_counter += 1
        if check_counter == 9:
            try:
                cursor.execute(insert_statement,(register_name.get(), register_pwd.get(), register_mobile.get(), var.get(), register_address.get(), register_email.get()))
                db.commit()
                messagebox.showinfo('Confirmation', 'You have successfully registered!')
            except Exception as e:
                messagebox.showerror('', e)
        else:
            messagebox.showerror('Error', warn)

    ws = tkinter.Tk()
    ws.title('User Registration')
    ws.config(bg='#0B5A81')
    f = ('Times', 14)
    var = tkinter.StringVar()
    var.set('Male')

    right_frame = tkinter.Frame(
        ws, 
        bd=2, 
        bg='#CCCCCC',
        relief=tkinter.SOLID, 
        padx=10, 
        pady=10
        )

    tkinter.Label(
        right_frame, 
        text="Enter Name", 
        bg='#CCCCCC',
        font=f
        ).grid(row=0, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Enter Email", 
        bg='#CCCCCC',
        font=f
        ).grid(row=1, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Phone Number", 
        bg='#CCCCCC',
        font=f
        ).grid(row=2, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Enter Address", 
        bg='#CCCCCC',
        font=f
        ).grid(row=3, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Select Gender", 
        bg='#CCCCCC',
        font=f
        ).grid(row=4, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Enter Password", 
        bg='#CCCCCC',
        font=f
        ).grid(row=5, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame, 
        text="Re-Enter Password", 
        bg='#CCCCCC',
        font=f
        ).grid(row=6, column=0, sticky=tkinter.W, pady=10)

    gender_frame = tkinter.LabelFrame(
        right_frame,
        bg='#CCCCCC',
        padx=10, 
        pady=10,
        )

    register_name = tkinter.Entry(
        right_frame, 
        font=f
        )

    register_email = tkinter.Entry(
        right_frame, 
        font=f
        )

    register_mobile = tkinter.Entry(
        right_frame, 
        font=f
        )
    
    register_address = tkinter.Entry(
        right_frame, 
        font=f
        )


    male_rb = tkinter.Radiobutton(
        gender_frame, 
        text='Male',
        bg='#CCCCCC',
        variable=var,
        value='Male',
        font=('Times', 10),
        
    )

    female_rb = tkinter.Radiobutton(
        gender_frame,
        text='Female',
        bg='#CCCCCC',
        variable=var,
        value='Female',
        font=('Times', 10),
    
    )

    others_rb = tkinter.Radiobutton(
        gender_frame,
        text='Other',
        bg='#CCCCCC',
        variable=var,
        value='Other',
        font=('Times', 10)
    
    )

    register_pwd = tkinter.Entry(
        right_frame, 
        font=f,
        show='*'
    )
    pwd_again = tkinter.Entry(
        right_frame, 
        font=f,
        show='*'
    )

    register_btn = tkinter.Button(
        right_frame, 
        width=15, 
        text='Register', 
        font=f, 
        relief=tkinter.SOLID,
        cursor='hand2',
        command=validate_signup
    )

    register_name.grid(row=0, column=1, pady=10, padx=20)
    register_email.grid(row=1, column=1, pady=10, padx=20) 
    register_mobile.grid(row=2, column=1, pady=10, padx=20)
    register_address.grid(row=3, column=1, pady=10, padx=20)
    register_pwd.grid(row=5, column=1, pady=10, padx=20)
    pwd_again.grid(row=6, column=1, pady=10, padx=20)
    register_btn.grid(row=7, column=1, pady=10, padx=20)
    right_frame.pack()
    gender_frame.grid(row=4, column=1, pady=10, padx=20)
    male_rb.pack(expand=True, side=tkinter.LEFT)
    female_rb.pack(expand=True, side=tkinter.LEFT)
    others_rb.pack(expand=True, side=tkinter.LEFT)

    ws.mainloop()
    return 

def LoginPage():
    login_screen = tkinter.Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    tkinter.Label(login_screen, text="Please enter login details").pack()
    tkinter.Label(login_screen, text="").pack()
    tkinter.Label(login_screen, text="user ID").pack()
    username_login_entry = tkinter.Entry(login_screen, textvariable="username")
    username_login_entry.pack()
    tkinter.Label(login_screen, text="").pack()
    tkinter.Label(login_screen, text="password").pack()
    password__login_entry = tkinter.Entry(login_screen, textvariable="password", show= '*')
    password__login_entry.pack()
    tkinter.Label(login_screen, text="").pack()
    tkinter.Button(login_screen, text="Login", width=10, height=1).pack()
    login_screen.mainloop()

def init_mongo():
    with open('items.json') as i:
        i_data = json.load(i)
    with open('products.json') as p:
        p_data = json.load(p)
    
    items.insert_many(i_data)
    products.insert_many(p_data)

def create_db_mysql():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE oshes")
    mydb.close()

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

def create_indexes_mongo():
    #simple search
    items.drop_indexes()
    items.create_index([("Category", TEXT), ("Model", TEXT)])
    return


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="oshes"
    )
mycursor = mydb.cursor()
#init_mongo()
#create_indexes_mongo()
#create_db_mysql()
#init_mysql()
#print(list(items.find({"$text": { "$search" : "Light1"}})))
#LoginPage()
CustomerSignUpPage(mycursor, mydb)
