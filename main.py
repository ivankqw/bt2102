import tkinter
from tkinter.constants import CENTER, TRUE
import tkinter.messagebox as messagebox
from tkscrolledframe import ScrolledFrame
from PIL import ImageTk, Image

import datetime
import mysql.connector
import re
from tkinter import StringVar, Tk, ttk
import mysql.connector
from mysql.connector.errors import OperationalError
from pymongo import MongoClient
from pymongo import TEXT
import json
import pandas as pd
from sqlalchemy import create_engine
import setup

def LandingPage(root):
    """ main_screen = root
    main_screen.title("OSHES app")
    main_screen.config(bg='#0B5A81')
    main_screen.grid()
    tkinter.Label(text="Welcome to OSHES :)", width="300",
                  height="2", font=("Calibri", 13)).pack()
    tkinter.Label(text="", bg='#0B5A81').pack()
    tkinter.Button(text="Customer Registration", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2',command= lambda: changepage("registerCustomer")).pack()
    tkinter.Label(text="", bg='#0B5A81').pack()
    tkinter.Button(text="Customer Login", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2',command= lambda: changepage("loginCustomer")).pack()
    tkinter.Label(text="", bg='#0B5A81').pack()
    tkinter.Button(text="Admin Registration", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2', command= lambda: changepage("registerAdmin")).pack()
    tkinter.Label(text="", bg='#0B5A81').pack()
    tkinter.Button(text="Admin Login", height="2", width="30", relief=tkinter.SOLID,cursor='hand2', command= lambda: changepage("loginAdmin")).pack() """
    root.configure(bg="#ffffff")
    root.title("OSHES app")

    canvas = tkinter.Canvas(
        root,
        bg="#ffffff",
        height=700,
        width=1040,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)
    canvas.update()

    background_img = ImageTk.PhotoImage(file=f"background.png")
    background = canvas.create_image(
        473, 350,
        image=background_img)

    img0 = ImageTk.PhotoImage(file=f"img0.png")
    customer_reg = tkinter.Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: changepage("registerCustomer"),
        relief="flat")

    customer_reg.place(
        x=600, y=247,
        width=400,
        height=67)

    img1 = ImageTk.PhotoImage(file=f"img1.png")
    admin_log = tkinter.Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: changepage("loginAdmin"),
        relief="flat")

    admin_log.place(
        x=600, y=503,
        width=400,
        height=67)

    img2 = ImageTk.PhotoImage(file=f"img2.png")
    admin_reg = tkinter.Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: changepage("registerAdmin"),
        relief="flat")

    admin_reg.place(
        x=600, y=417,
        width=400,
        height=67)

    img3 = ImageTk.PhotoImage(file=f"img3.png")
    customer_log = tkinter.Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: changepage("loginCustomer"),
        relief="flat")

    customer_log.place(
        x=600, y=332,
        width=400,
        height=67)
    root.mainloop()
    return


def AdminSignUpPage(root, cursor, db):
    def validate_signup_admin():
        check_counter = 0
        warn = ""
        insert_statement = "INSERT INTO Administrator (adminName, gender, phoneNumber, adminPassword) VALUES (%s, %s, %s, %s)"
        if register_name.get() == "":
            warn += "\n"
            warn += "Name cannot be empty!"
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
        if var.get() == "":
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
        if check_counter == 7:
            try:
                cursor.execute(insert_statement, (register_name.get(
                ), var.get(), register_mobile.get(), register_pwd.get()))
                db.commit()
                adminID = str(cursor.lastrowid)
                register_name.delete(0, tkinter.END)
                register_mobile.delete(0, tkinter.END)
                register_pwd.delete(0, tkinter.END)
                pwd_again.delete(0, tkinter.END)
                messagebox.showinfo(
                    'Confirmation', 'You have successfully registered! Your Admin ID is ' + adminID + '. Please go back to the main page to Log in as an Administrator!')
                tkinter.Button(text="Admin Login", height="2", width="30", relief=tkinter.SOLID,
                               cursor='hand2', command=lambda: changepage("loginAdmin")).pack()
            except Exception as e:
                messagebox.showerror('', e)
        else:
            messagebox.showerror('Error', warn)

    ws = root
    ws.title('Administrator Registration')
    ws.config(bg='#e6bbad')
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
        text="Phone Number",
        bg='#CCCCCC',
        font=f
    ).grid(row=1, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame,
        text="Select Gender",
        bg='#CCCCCC',
        font=f
    ).grid(row=2, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame,
        text="Enter Password",
        bg='#CCCCCC',
        font=f
    ).grid(row=3, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        right_frame,
        text="Re-Enter Password",
        bg='#CCCCCC',
        font=f
    ).grid(row=4, column=0, sticky=tkinter.W, pady=10)

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

    register_mobile = tkinter.Entry(
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
        command=validate_signup_admin
    )

    tkinter.Label(text="Welcome New Admin! :)", width="300",
                  height="2", font=("Calibri", 13)).pack()
    tkinter.Label(text="", bg='#e6bbad').pack()
    register_name.grid(row=0, column=1, pady=10, padx=20)
    register_mobile.grid(row=1, column=1, pady=10, padx=20)
    register_pwd.grid(row=3, column=1, pady=10, padx=20)
    pwd_again.grid(row=4, column=1, pady=10, padx=20)
    register_btn.grid(row=5, column=1, pady=10, padx=20)
    right_frame.pack()
    gender_frame.grid(row=2, column=1, pady=10, padx=20)
    male_rb.pack(expand=True, side=tkinter.LEFT)
    female_rb.pack(expand=True, side=tkinter.LEFT)
    others_rb.pack(expand=True, side=tkinter.LEFT)
    tkinter.Button(text="Back to Home", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("landing")).pack(side=tkinter.BOTTOM)
    return


def CustomerSignUpPage(root, cursor, db):
    def validate_signup():
        check_counter = 0
        warn = ""
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        insert_statement = "INSERT INTO Customer (customerName, customerPassword, phoneNumber, gender, address, email) VALUES (%s, %s, %s, %s, %s, %s)"
        if register_name.get() == "":
            warn += "\n"
            warn += "Name cannot be empty!"
        else:
            check_counter += 1
        check_counter = 0

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
        if var.get() == "":
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
                cursor.execute(insert_statement, (register_name.get(), register_pwd.get(
                ), register_mobile.get(), var.get(), register_address.get(), register_email.get()))
                db.commit()
                customerID = str(cursor.lastrowid)
                register_name.delete(0, tkinter.END)
                register_email.delete(0, tkinter.END)
                register_mobile.delete(0, tkinter.END)
                register_address.delete(0, tkinter.END)
                register_pwd.delete(0, tkinter.END)
                pwd_again.delete(0, tkinter.END)
                messagebox.showinfo(
                    'Confirmation', 'You have successfully registered! Your Customer ID is ' + customerID + '. Please go back to the main page to log in as a Customer!')
                tkinter.Button(text="Customer Login", height="2", width="30", relief=tkinter.SOLID,
                               cursor='hand2', command=lambda: changepage("loginCustomer")).pack()
            except Exception as e:
                messagebox.showerror('', e)
        else:
            messagebox.showerror('Error', warn)

    ws = root
    ws.title('Customer Registration')
    ws.config(bg='#add8e6')
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

    tkinter.Label(text="Welcome New Customer! :)", width="300",
                  height="2", font=("Calibri", 13)).pack()
    tkinter.Label(text="", bg='#add8e6').pack()
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
    tkinter.Button(text="Back to Home", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("landing")).pack(side=tkinter.BOTTOM)
    return


def CustomerLoginPage(root, cursor):
    def validate_login():
        check_counter = 0
        warn = ""
        if email_tf.get() == "":
            warn += "\n"
            warn += "Please enter an ID!"
        else:
            check_counter += 1
        if pwd_tf.get() == "":
            warn += "\n"
            warn += "Please enter a password!"
        else:
            check_counter += 1

        selection_statement = "SELECT customerID, customerName, email, customerPassword FROM Customer WHERE customerID = %s AND customerPassword = %s"

        if check_counter == 2:
            try:
                cursor.execute(selection_statement,
                               (email_tf.get(), pwd_tf.get()))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showinfo(
                        'Error', 'Invalid Email and/or Password')
                else:
                    customerID = row[0]
                    customerName = row[1]
                    messagebox.showinfo(
                        "Logged in successfully. ", "Welcome, " + customerName + " !")
                    cursor.reset()
                    changepage("customerHomePage", customerID)
            except Exception as e:
                messagebox.showerror('Error', e)
        else:
            messagebox.showerror('Error', warn)

    ws = root
    ws.title('Customer Login')
    ws.config(bg='#add8e6')

    f = ('Times', 14)

    left_frame = tkinter.Frame(
        ws,
        bd=2,
        bg='#CCCCCC',
        relief=tkinter.SOLID,
        padx=10,
        pady=10
    )

    tkinter.Label(
        left_frame,
        text="Enter your Customer ID",
        bg='#CCCCCC',
        font=f).grid(row=0, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        left_frame,
        text="Enter your Password",
        bg='#CCCCCC',
        font=f
    ).grid(row=1, column=0, pady=10)

    email_tf = tkinter.Entry(
        left_frame,
        font=f
    )
    pwd_tf = tkinter.Entry(
        left_frame,
        font=f,
        show='*'
    )
    login_btn = tkinter.Button(
        left_frame,
        width=15,
        text='Login',
        font=f,
        relief=tkinter.SOLID,
        cursor='hand2',
        command=validate_login
    )

    tkinter.Label(text="Welcome existing customer! :)",
                  width="300", height="2", font=("Calibri", 13)).pack()
    tkinter.Label(text="", bg='#add8e6').pack()
    email_tf.grid(row=0, column=1, pady=10, padx=20)
    pwd_tf.grid(row=1, column=1, pady=10, padx=20)
    login_btn.grid(row=2, column=1, pady=10, padx=20)
    left_frame.pack()
    tkinter.Button(text="Back to Home", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("landing")).pack(side=tkinter.BOTTOM)
    return


def AdminLoginPage(root, cursor):

    def validate_login_a():
        check_counter = 0
        warn = ""
        if phone_tf.get() == "":
            warn += "\n"
            warn += "Please enter a phone number!"
        else:
            check_counter += 1
        if pwd_tf.get() == "":
            warn += "\n"
            warn += "Please enter a password!"
        else:
            check_counter += 1

        selection_statement = "SELECT adminID, adminName, phoneNumber, adminPassword FROM Administrator WHERE adminID = %s AND adminPassword = %s"

        if check_counter == 2:
            try:
                cursor.execute(selection_statement,
                               (phone_tf.get(), pwd_tf.get()))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showinfo(
                        'Error', 'Invalid Phone Number and/or Password')
                else:
                    adminID = row[0]
                    adminName = row[1]
                    messagebox.showinfo(
                        "Logged in successfully. ", "Welcome, " + adminName + " !")
                    cursor.reset()
                    changepage("adminHomePage", adminID)
            except Exception as e:
                messagebox.showerror('Error', e)
        else:
            messagebox.showerror('Error', warn)

    ws = root
    ws.title('Administrator Login')
    ws.config(bg='#e6bbad')

    #for x in myresult:
    #    tree.insert("", "end", values = x)
    #tree.grid(row = 1, column = 0)
    f = ('Times', 14)
   
    left_frame = tkinter.Frame(
        ws,
        bd=2,
        bg='#CCCCCC',
        relief=tkinter.SOLID,
        padx=10,
        pady=10
    )

    tkinter.Label(
        left_frame,
        text="Enter your Admin ID",
        bg='#CCCCCC',
        font=f).grid(row=0, column=0, sticky=tkinter.W, pady=10)

    tkinter.Label(
        left_frame,
        text="Enter your Password",
        bg='#CCCCCC',
        font=f
    ).grid(row=1, column=0, pady=10)

    phone_tf = tkinter.Entry(
        left_frame,
        font=f
    )
    pwd_tf = tkinter.Entry(
        left_frame,
        font=f,
        show='*'
    )
    login_btn = tkinter.Button(
        left_frame,
        width=15,
        text='Login',
        font=f,
        relief=tkinter.SOLID,
        cursor='hand2',
        command=validate_login_a
    )

    tkinter.Label(text="Welcome existing Administrator! :)",
                  width="300", height="2", font=("Calibri", 13)).pack()
    tkinter.Label(text="", bg='#e6bbad').pack()
    phone_tf.grid(row=0, column=1, pady=10, padx=20)
    pwd_tf.grid(row=1, column=1, pady=10, padx=20)
    login_btn.grid(row=2, column=1, pady=10, padx=20)
    left_frame.pack()
    tkinter.Button(text="Back to Home", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("landing")).pack(side=tkinter.BOTTOM)
    return


def AdminHomePage(root, cursor, adminID):
    main_screen = root
    main_screen.title("OSHES app")
    main_screen.config(bg='#e6bbad')
    main_screen.grid()

    tkinter.Label(text="Welcome to Admin's Home Page :)",
                  width="300", height="2", font=("Calibri", 13)).pack()
    tkinter.Label(text="", bg='#e6bbad').pack()
    tkinter.Button(text="Search Items", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("adminSearchAllOrOne", adminID)).pack()
    tkinter.Label(text="", bg='#e6bbad').pack()
    tkinter.Button(text="Inventory", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("inventoryHomePage", adminID)).pack()
    tkinter.Label(text="", bg='#e6bbad').pack()
    tkinter.Button(text="Service Statuses", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("serviceStatusesHomePage", adminID)).pack()
    tkinter.Label(text="", bg='#e6bbad').pack()
    tkinter.Button(text="Unpaid", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("unpaidHomePage", adminID)).pack()
    
    tkinter.Label(text="", bg='#e6bbad').pack()
    def areThereRequests():
        select_requests = "SELECT * FROM request WHERE requestStatus = 'Submitted' OR requestStatus = 'In progress'"
        cursor.execute(select_requests)
        all_requests = cursor.fetchall()
        cursor.reset()
        if all_requests == []:
            return False
        return True
    tkinter.Button(text="Approve", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("approveHomePage", adminID) if areThereRequests() else messagebox.showinfo('Good news!', 'No requests waiting to be approved')).pack()
    tkinter.Label(text="", bg='#e6bbad').pack()
    def areThereItemsToService():
        
        select_inprogitems = "SELECT * FROM item WHERE serviceStatus = 'In progress'"
        cursor.execute(select_inprogitems)
        itemsinprog = cursor.fetchall()
        cursor.reset()
        if itemsinprog == []:
            return False
        
        return True
        
    tkinter.Button(text="Service Items", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("serviceItemsPage", adminID) if areThereItemsToService() else messagebox.showinfo('Good news!', 'No items im progress of service')).pack()
    tkinter.Label(text="", bg='#e6bbad').pack()
    ##INITIALIZE DATA
    def init_database():
        def popup_table(root):
            popup = tkinter.Toplevel(root)
            popup.wm_title("Database Initialized!")
            popup.tkraise(root) # so message is on top of the main window
            ##tkinter.Label(popup, text=msg).pack(side="top", fill="x", pady=10)
            sql1 = "SELECT A.productID, A.Sold, B.Unsold \
            FROM (SELECT productID, COUNT(purchaseStatus) as Sold \
            FROM item \
            WHERE purchaseStatus = 'Sold' \
            GROUP by productID) AS A \
            CROSS JOIN(SELECT productID, COUNT(purchaseStatus) as Unsold \
            FROM item \
            WHERE purchaseStatus = 'Unsold' \
            GROUP by productID) AS B \
            ON A.productID = B.productID"
            cursor.execute(sql1)
            myresult = cursor.fetchall()

            style = ttk.Style()
            style.theme_use('default')
            tree = ttk.Treeview(popup, columns=(
                'IID', 'Number of SOLD items', 'Number of UNSOLD items'), show='headings')

            tree.column("#1", anchor=CENTER, width=195)
            tree.heading('#1', text='IID')
            tree.column("#2", anchor=CENTER, width=195)
            tree.heading('#2', text='Number of SOLD items')
            tree.column("#3", anchor=CENTER, width=195)
            tree.heading('#3', text='Number of UNSOLD items')

            for x in myresult:
                tree.insert("", "end", values=x)
            tree.pack()
            tkinter.Button(popup, text="Close", command = popup.destroy).pack()
        def init_mysql_inp(mycursor):
            with open('reinitMYSQL.sql', 'r') as SQLscript:
                SQLcommands = SQLscript.read().split(';')
                for command in SQLcommands:
                    mycursor.execute(command)

        init_mysql_inp(cursor)
        setup.items_info_to_sql(password=MYSQL_PASSWORD)
        setup.products_info_to_sql(password=MYSQL_PASSWORD)
        popup_table(root)

    tkinter.Button(text="Initialize Databases", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: init_database()).pack()
    tkinter.Label(text="", bg='#e6bbad').pack()    
    tkinter.Button(text="Logout", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("landing")).pack(side=tkinter.BOTTOM)

    return

def AdminSearchAllOrOnePage(root, cursor, adminID):
    for widget in root.winfo_children():
        widget.destroy()

    def search_item(itemID, adminID):
        if len(itemID) != 4 or not list(items.find({"ItemID": itemID})):
            messagebox.showerror(
                title="Error", message="Please enter a valid Item ID")
        else:
            changepage("adminSearchForOnePage", itemID, adminID)

    ws = root
    ws.title('Admin - Home')
    ws.config(bg='#add8e6')
    #tkinter.Label(ws, text="Welcome " + customerName + " [ID:" + str(
        #currCustomerID) + "]", width="300", height="2", font=("Calibri", 13)).pack()
    tkinter.Label(ws, text="", bg='#add8e6').pack()
    tkinter.Button(ws, text="Search multiple items", height="2", width="30",
                   relief=tkinter.SOLID, command=lambda: changepage("adminSearchAllPage", adminID)).pack()
    tkinter.Label(ws, text="", bg='#add8e6').pack()
    tkinter.Label(ws, text="Please enter Item ID",
                  width="300", height="2", font=("Calibri", 13)).pack()
    # for buy entry
    f = ('Times', 14)
    tkinter.Label(ws, text="Enter item ID here", bg='#CCCCCC', font=f)
    itemid = tkinter.Entry(ws, font=f)
    itemid.pack()
    tkinter.Button(ws, text="Search", height="2", width="30",
                   relief=tkinter.SOLID, command=lambda: search_item(itemid.get(), adminID)).pack()
    tkinter.Label(ws, text="", bg='#add8e6').pack()
    tkinter.Button(text="Back to Admin Home Page", height="2", width="30", bg="#e6d8ad",
                   relief=tkinter.SOLID, command=lambda: changepage("adminHomePage", adminID)).pack()
    return 

def AdminSearchForOnePage(root, cursor, itemID, adminID):
    main_screen = root
    main_screen.title("Search Result")
    main_screen.config(bg='#e6bbad')
    main_screen.grid()

    tkinter.Label(text="Here is the item you're looking for :)",
                        width="300", height="2", font=("Calibri", 13)).pack()
    selection_statement = "SELECT purchaseStatus FROM item WHERE itemID = '%s'"
    cursor.execute(selection_statement % itemID)
    purchase_status_info = cursor.fetchall()
    cursor.reset()

    style = ttk.Style()
    style.theme_use("default")
    columns = ('ItemID', 'Category', 'Model', 'Color', 'Factory', 'PowerSupply',
            'PurchaseStatus', 'ProductionYear', 'Price', 'Warranty (months)', 'Cost') 
    tree = ttk.Treeview(root, columns=columns, show='headings')
    for i in range(len(columns)):
        tree.column("#{}".format(i+1), anchor=CENTER,
                            minwidth=0, width=100, stretch=tkinter.NO)
        tree.heading("#{}".format(i+1), text=columns[i])

    #item = items.find({"ItemID" : itemID})
    for item in items.find({"ItemID" : itemID}):
        cat = item['Category']
        mod = item['Model']
        col = item['Color']
        fact = item['Factory']
        powersup = item['PowerSupply']
        purchasestatus = purchase_status_info[0]
        prodyear = item['ProductionYear']
        price = itemPriceWarrantyCost(cat, mod)[0]
        warranty = itemPriceWarrantyCost(cat, mod)[1]
        cost = itemPriceWarrantyCost(cat, mod)[2]
        values = (itemID, cat, mod, col, fact, powersup, purchasestatus, prodyear, price, warranty, cost)
        tree.insert("", "end", values=values)   

    tkinter.Button(text="Back", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                cursor='hand2', command= lambda: AdminSearchAllOrOnePage(root, cursor, adminID)).pack(side=tkinter.TOP)

def AdminSearchAllPage(root, cursor, adminID):
    for widget in root.winfo_children():
        widget.destroy()
    ws = root
    ws.title('Choose a category!')
    ws.wm_geometry("1040x900")
    ws.config(bg='#add8e6')
    '''# Category
    categories = [default_category, "Lights", "Locks"]
    category = tkinter.StringVar()
    category.set(categories[0])
    dropcat = tkinter.OptionMenu(root, category, *categories)
    dropcat.pack()

    # Model
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Light model:", bg='#add8e6').pack()

    lights = [default_category, "Light1", "Light2", "SmartHome1"]
    light = tkinter.StringVar()
    light.set(lights[0])
    droplight = tkinter.OptionMenu(root, light, *lights)
    droplight.pack()

    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Lock model:", bg='#add8e6').pack()
    locks = [default_category, "Safe1", "Safe2", "Safe3", "SmartHome1"]
    lock = tkinter.StringVar()
    lock.set(locks[0])
    droplock = tkinter.OptionMenu(root, lock, *locks)
    droplock.pack()'''

    # Category

    tkinter.Label(text="Select Category:", bg='#add8e6').pack()
    default_category = "No option selected"

    def update_model_options(category_selected):
        menu = dropmodels['menu']
        menu.delete(0, 'end')
        if category_selected == 'Lights':
            selected_models = [default_category, 'Light1', 'Light2', 'SmartHome1']
        elif category_selected == 'Locks':
            selected_models = [default_category, 'Safe1', 'Safe2', 'Safe3', 'SmartHome1']
        else:
            selected_models = [default_category, 'Light1', 'Light2', 'Safe1', 'Safe2', 'Safe3', 'SmartHome1']
        # models.set('No option selected')
        for each_model in selected_models:
            menu.add_command(label=each_model, command=lambda x=each_model: on_model_change(x))

    category = tkinter.StringVar()
    category_choices = [default_category, 'Lights', 'Locks']
    category.set(category_choices[0])
    dropcat = tkinter.OptionMenu(root, category, *category_choices, command=update_model_options)
    # formatting: dropcat.config(bg='white', fg='black', width=15, relief=tkinter.GROOVE)
    # dropcat.place(x=130, y=110)
    dropcat.pack()
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Model:", bg='#add8e6').pack()

    # Models
    def on_model_change(model_selected):
        models.set(model_selected)

    models = tkinter.StringVar()
    model_choices = [default_category, 'Light1', 'Light2', 'Safe1', 'Safe2', 'Safe3', 'SmartHome1']
    models.set(model_choices[0])
    dropmodels = tkinter.OptionMenu(root, models, *model_choices, command=on_model_change)
    dropmodels.pack()
    #dropmodels.config(bg='white', fg='black', width=15, relief=tkinter.GROOVE)
    #dropmodels.place(x=130, y=150)

    # Advanced options

    # Colour

    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Color:", bg='#add8e6').pack()
    colors = [default_category, "White", "Blue",
              "Yellow", "Green", "Black"]
    color = tkinter.StringVar()
    color.set('No option selected')
    dropcolor = tkinter.OptionMenu(root, color, *colors)
    dropcolor.pack()

    # Factory
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Factory:", bg='#add8e6').pack()
    factories = [default_category, "Malaysia", "China", "Philippines"]
    factory = tkinter.StringVar()
    factory.set('No option selected')
    dropfactory = tkinter.OptionMenu(root, factory, *factories)
    dropfactory.pack()

    # Power supply
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Power Supply:", bg='#add8e6').pack()
    powersupplies = [default_category, "Battery", "USB"]
    powersupply = tkinter.StringVar()
    powersupply.set('No option selected')
    droppowersupply = tkinter.OptionMenu(root, powersupply, *powersupplies)
    droppowersupply.pack()

    # Production year
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Production Year:", bg='#add8e6').pack()
    prodyears = [default_category, "2014", "2015",
                 "2016", "2017", "2018", "2019", "2020", ]
    prodyear = tkinter.StringVar()
    prodyear.set('No option selected')
    dropprodyear = tkinter.OptionMenu(root, prodyear, *prodyears)
    dropprodyear.pack()

    # Price
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Price Range:", bg='#add8e6').pack()
    tkinter.Label(text="Min:", bg='#add8e6').pack()
    minprice = StringVar(value = '0')
    maxprice = StringVar(value = '200')
    pricemin = tkinter.Entry(textvariable=minprice)
    pricemin.pack()
    tkinter.Label(text="Max:", bg='#add8e6').pack()
    pricemax = tkinter.Entry(textvariable=maxprice)
    pricemax.pack()

    advanced_options = {
        'Color': color, 
        'Factory': factory,
        "PowerSupply": powersupply, 
        "ProductionYear": prodyear,
        "MinPrice": minprice,
        "MaxPrice": maxprice
        }

    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="", bg='#add8e6').pack()

    tkinter.Button(text="Search", height="2", width="30", relief=tkinter.SOLID,
                   command=lambda: AdminSimpleSearchResult(root, cursor, category.get(), (models.get() if category.get() == "Lights" else models.get()), advanced_options, adminID) 
                   ).pack()
                   ##if areThereSearchResults() else messagebox.showinfo('No search results!')
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Button(text="Back", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command= lambda: AdminSearchAllOrOnePage(root, cursor, adminID)).pack(side=tkinter.TOP)
    return

def AdminSimpleSearchResult(root, cursor, cat, mod, advanced_options, adminID):
    for widget in root.winfo_children():
        widget.destroy()
    ws = root
    ws.title('Search results')
    ws.config(bg='#add8e6')
    f = ('Calibri', 13)

    color = advanced_options['Color'].get()
    factory = advanced_options['Factory'].get()
    powerSupply = advanced_options['PowerSupply'].get()
    prodYear = advanced_options['ProductionYear'].get()
    try:
        minPrice = int(advanced_options['MinPrice'].get())
        maxPrice = int(advanced_options['MaxPrice'].get())
    except:
        messagebox.showerror(title="Invalid Price Range", message="Price range should be from 0 to 200 ($)")
        AdminSearchAllOrOnePage(root, cursor, adminID)
    else:
        if (minPrice < 0 or maxPrice < 0 or minPrice > maxPrice):
            messagebox.showerror(title="Invalid Price Range", message="Price range should be from 0 to 200 ($)")
            AdminSearchAllOrOnePage(root, cursor, adminID)
    
    default_category = "No option selected"
    search_string = ""
    if cat != default_category:
        search_string += "Category: " + cat + ", "
    if mod != default_category:
        search_string += "Model: " + mod + ", "
    if color != default_category:
        search_string += "Color: " + color + ", "
    if factory != default_category:
        search_string += "Factory: " + factory + ", "
    if powerSupply != default_category:
        search_string += "powerSupply: " + powerSupply + ", "
    if prodYear != default_category:
        search_string += "productionYear: " + prodYear + ", "
    search_string += "Price range: {} to {}, ".format(minPrice, maxPrice)
    tkinter.Label(text="Search results for {}".format(
        search_string[:-2]), bg='#CCCCCC', font=f).grid(row=0, column=0)

    # display search result below

    style = ttk.Style()
    style.theme_use("default")
    columns = ('ItemID', 'Category', 'Model', 'Color', 'Factory', 'PowerSupply',
               'PurchaseStatus', 'ProductionYear', 'Price', 'Warranty (months)', 'Cost') 
    tree = ttk.Treeview(root, columns=columns, show='headings')
    for i in range(len(columns)):
        tree.column("#{}".format(i+1), anchor=CENTER,
                    minwidth=0, width=93, stretch=tkinter.NO)
        tree.heading("#{}".format(i+1), text=columns[i])

    item_sold_count = 0
    # Creating of MongoDB query dict
    find_dict = {}
    if cat != default_category:
        find_dict['Category'] = cat
    if mod != default_category:
        find_dict['Model'] = mod
    if color != default_category:
        find_dict['Color'] = color
    if factory != default_category:
        find_dict['Factory'] = factory
    if powerSupply != default_category:
        find_dict['PowerSupply'] = powerSupply
    if prodYear != default_category:
        find_dict['ProductionYear'] = prodYear
    

    for item in items.find(find_dict):
        if itemSold(cursor, item['ItemID']):
            item_sold_count += 1
        values = (
            item['ItemID'],
            item['Category'],
            item['Model'],
            item['Color'],
            item['Factory'],
            item['PowerSupply'],
            item['PurchaseStatus'],
            item['ProductionYear'],
            itemPriceWarrantyCost(item['Category'], item['Model'])[0],
            itemPriceWarrantyCost(item['Category'], item['Model'])[1],
            itemPriceWarrantyCost(item['Category'], item['Model'])[2]
        )
        price = int(values[-2])
        if price >= minPrice and price <= maxPrice:
            tree.insert("", "end", values=values)

    tree.grid(row=1, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(ws, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')

    tkinter.Label(text="Number of sold items: " +
                    str(item_sold_count), bg='#FFFFFF').grid(row=3, column=0)

    tkinter.Button(text="Back to search", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: AdminSearchAllOrOnePage(root, cursor, adminID)).grid(row=4, column=0)
    return

def InventoryHomePage(root, mycursor, adminID):
    #by model
    sql1 = "SELECT A.category, A.model, A.Sold, B.Unsold\
    FROM (SELECT category, model, COUNT(purchaseStatus) as Sold\
    FROM item\
    WHERE purchaseStatus = 'Sold'\
    GROUP by category, model) AS A\
    LEFT JOIN(SELECT category, model, COUNT(purchaseStatus) as Unsold\
    FROM item\
    WHERE purchaseStatus = 'Unsold'\
    GROUP by category, model) AS B\
    ON A.model = B.model and A.category = B.category;"

    #by category
    sql2 = "SELECT A.category, A.Sold, B.Unsold FROM (SELECT category, COUNT(purchaseStatus) as Sold\
    FROM item WHERE purchaseStatus = 'Sold'\
    GROUP by category) AS A LEFT JOIN(SELECT category, COUNT(purchaseStatus) as Unsold\
    FROM item WHERE purchaseStatus = 'Unsold'\
    GROUP by category) AS B ON A.category = B.category;"

    mycursor.execute(sql1)
    myresult1 = mycursor.fetchall()

    tkinter.Label(text="Products by model", width=30, height="2",
                  font=("Calibri", 13)).grid(row=0, column=0)

    style = ttk.Style()
    style.theme_use('default')
    tree = ttk.Treeview(columns=(
        'Category','Model', 'Number of SOLD items', 'Number of UNSOLD items'), show='headings')

    root.title('Inventory')
    tree.column("#1", anchor=CENTER, width=195)
    tree.heading('#1', text='Category')
    tree.column("#2", anchor=CENTER, width=195)
    tree.heading('#2', text='Model')
    tree.column("#3", anchor=CENTER, width=195)
    tree.heading('#3', text='Number of SOLD items')
    tree.column("#4", anchor=CENTER, width=195)
    tree.heading('#4', text='Number of UNSOLD items')

    for x in myresult1:
        y = list(x)
        if y[2] is None:
            y[2] = 0
        if y[3] is None:
            y[3] = 0
        x = tuple(y)
        tree.insert("", "end", values=x)
    tree.grid(row=1, column=0)

    scrollbar = ttk.Scrollbar(root, orient=tkinter.VERTICAL)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky="ns")



    mycursor.execute(sql2)
    myresult2 = mycursor.fetchall()

    tkinter.Label(text="Products by category", width=30, height="2",
                  font=("Calibri", 13)).grid(row=3, column=0)

    style = ttk.Style()
    style.theme_use('default')
    tree = ttk.Treeview(columns=(
        'Category', 'Number of SOLD items', 'Number of UNSOLD items'), show='headings')

    #root.title('Inventory')
    tree.column("#1", anchor=CENTER, width=260)
    tree.heading('#1', text='Category')
    tree.column("#2", anchor=CENTER, width=260)
    tree.heading('#2', text='Number of SOLD items')
    tree.column("#3", anchor=CENTER, width=260)
    tree.heading('#3', text='Number of UNSOLD items')

    for x in myresult2:
        y = list(x)
        if y[1] is None:
            y[1] = 0
        if y[2] is None:
            y[2] = 0
        x = tuple(y)
        tree.insert("", "end", values=x)
    tree.grid(row=4, column=0)

    scrollbar = ttk.Scrollbar(root, orient=tkinter.VERTICAL)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=4, column=1, sticky="ns")

    tkinter.Button(text="Back to Admin", height="2", width="20", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("adminHomePage", adminID)).grid(row=5, column=0)



def ServiceStatusesPage(root, mycursor, adminID):
    sql2 = "SELECT itemID,productID,serviceStatus FROM item\
    WHERE serviceStatus = 'In progress' OR serviceStatus = 'Waiting for approval'\
    UNION\
    SELECT 'Total items under service', '', COUNT(*) FROM item\
    WHERE serviceStatus = 'In progress' OR serviceStatus = 'Waiting for approval'\
    ORDER by itemID"

    mycursor.execute(sql2)
    myresult = mycursor.fetchall()


    tkinter.Label(text="Items under service", width=30, height="2",
                  font=("Calibri", 13)).grid(row=0, column=0)

    style = ttk.Style()
    style.theme_use('default')
    tree = ttk.Treeview(columns=('Item ID', 'Product ID',
                        'Service Status'), show='headings')

    root.title('Items under service')
    tree.column("#1", anchor=CENTER, width=195)
    tree.heading('#1', text='Item ID')
    tree.column("#2", anchor=CENTER, width=195)
    tree.heading('#2', text='Product ID')
    tree.column("#3", anchor=CENTER, width=195)
    tree.heading('#3', text='Service Status')

    for x in myresult:
        tree.insert("", "end", values=x)
    tree.grid(row=1, column=0)

    scrollbar = ttk.Scrollbar(root, orient=tkinter.VERTICAL)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky="ns")

    tkinter.Button(text="Back to Admin", height="2", width="20", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("adminHomePage", adminID)).grid(row=2, column=0)


def UnpaidHomePage(root, mycursor, adminID):
    sql3 = "SELECT C.customerID, C.customerName, C.email, C.address\
        FROM customer AS C\
        INNER JOIN request AS R ON R.customerID = C.customerID\
        WHERE R.requestStatus = 'Submitted and Waiting for payment' "

    mycursor.execute(sql3)
    myresult = mycursor.fetchall()



    tkinter.Label(text="Customers with unpaid service fees", width=50,
                  height="2", font=("Calibri", 13)).grid(row=0, column=0, sticky='ew')

    style = ttk.Style()
    style.theme_use('default')
    tree = ttk.Treeview(columns=('Customer ID', 'Item ID',
                        'Request ID'), show='headings')

    root.title("Customers with unpaid service fees")
    tree.column("#1", anchor=CENTER, width=195)
    tree.heading('#1', text='Customer ID')
    tree.column("#2", anchor=CENTER, width=195)
    tree.heading('#2', text='Customer Name')
    tree.column("#3", anchor=CENTER, width=195)
    tree.heading('#3', text='Customer Email')

    for x in myresult:
        tree.insert("", "end", values=x)
    tree.grid(row=1, column=0)

    scrollbar = ttk.Scrollbar(orient=tkinter.VERTICAL)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky="ns")

    tkinter.Button(text="Back to Admin", height="2", width="20", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("adminHomePage", adminID)).grid(row=2, column=0)


def CustomerHomePage(root, cursor, customerID):
    cancelInvalidRequests()
    main_screen = root
    main_screen.title("OSHES app")
    main_screen.config(bg='#add8e6')
    main_screen.grid()

    tkinter.Label(text="Welcome to Customer's Home Page :)",
                  width="300", height="2", font=("Calibri", 13)).pack()
    tkinter.Label(text="", bg='#add8e6').pack()
    # uncomment end of the lines and remove pack() below when implemented these pages
    tkinter.Button(text="Buy Items", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("CustomerBuySearch", customerID)).pack()
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Button(text="Request for Item Service", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("customerRequestPage", customerID)).pack()
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Button(text="My Requests", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("customerAllRequestPage", customerID)).pack()
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Button(text="Cancel a Request", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("customerCancelRequestPage", customerID)).pack()
    def areThereMyItems():
        sql_statement = "SELECT * FROM item WHERE customerID = '%s' "
        cursor.execute(sql_statement % customerID)
        all_requests = cursor.fetchall()
        cursor.reset()
        if all_requests == []:
            return False
        return True
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Button(text="View My Items", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("myItemsPage", customerID) if areThereMyItems() else messagebox.showinfo('Oh no!', 'You did not purchase any items!')).pack()
    tkinter.Label(text="", bg='#add8e6').pack()
    def areTherePayments():
        select_payments = "SELECT * FROM request WHERE requestStatus = 'Submitted and Waiting for payment'"
        cursor.execute(select_payments)
        all_payments = cursor.fetchall()
        cursor.reset()
        if all_payments == []:
            return False
        return True
    tkinter.Button(text="Pay for Item Service", height="2", width="30", relief=tkinter.SOLID,
                   cursor='hand2',command= lambda: changepage("payServiceHomePage", customerID) if areTherePayments() else messagebox.showinfo(message = 'No payments currently needed!')).pack()
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Button(text="Logout", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("landing")).pack(side=tkinter.BOTTOM)
    tkinter.Label(text="", bg='#add8e6').pack()
    

    return


def approveAndUpdateRequestStatusAndTagAdminID(requestID, adminID, itemID): 
    updateRequestStatus = "UPDATE request SET requestStatus = 'Approved' WHERE requestID = %s and itemID = %s" 
    mycursor.execute(updateRequestStatus, (requestID, itemID)) 
    #tag adminID to requestID for request table 
    updateAdminID1 = "UPDATE request SET adminID = %s WHERE itemID = %s" 
    mycursor.execute(updateAdminID1, (adminID, itemID)) 
    #tag adminID in item table, not just request table 
    updateAdminID2 = "UPDATE item SET adminID = %s WHERE itemID = %s" 
    mycursor.execute(updateAdminID2, (adminID, itemID)) 
    #now item table will have admin id correspond to item id, then update servicestatus  
    updateServiceStatus = "UPDATE item SET serviceStatus = 'In progress' WHERE itemID = %s AND adminID = %s" 
    mycursor.execute(updateServiceStatus, (itemID, adminID)) 
    mydb.commit() 
    return 



def ApproveHomePage(root, cursor, adminID):
    # def approve_request():
    #   selected = tree.focus()
    #   temp = tree.item(selected, 'values')
    #   approve = "Approved"
    #   tree.item(selected, values=(temp[0], temp[1], approve, temp[3], temp[4], temp[5]))
    #   sql_statement = "UPDATE request SET requestStatus = 'Approved' WHERE requestID = %s"
    #   cursor.execute(sql_statement % temp[0]) #correct, just change comma to %
    #   mydb.commit() #need to commit if not mysql database would not be updated
    #   messagebox.showinfo("Success! ", "You have successfully approved the following: Request ID " + temp[0]) #messagebox after everything

    main_screen = root
    main_screen.title("OSHES app")
    main_screen.config(bg='#e6bbad')
    main_screen.grid()

    tkinter.Label(text="Here are the requests waiting for approval :)",
                  width="300", height="2", font=("Calibri", 13)).pack()
    selection_statement = "SELECT * FROM request WHERE requestStatus = 'Submitted' OR requestStatus = 'In progress'"
    cursor.execute(selection_statement)
    table_info = cursor.fetchall()
    cursor.reset()

    style = ttk.Style()
    style.theme_use('default')
    tree = ttk.Treeview(root, columns=('Request ID', 'Date of Request',
                        'Request Status', 'Customer ID', 'Admin ID', 'Item ID'), show='headings')
    tree.pack()

    root.title('Approval Page')
    tree.column('#1', anchor=CENTER, width='100')
    tree.heading('#1', text='Request ID')
    tree.column('#2', anchor=CENTER, width='100')
    tree.heading('#2', text='Date of Request')
    tree.column('#3', anchor=CENTER, width='100')
    tree.heading('#3', text='Request Status')
    tree.column('#4', anchor=CENTER, width='100')
    tree.heading('#4', text='Customer ID')
    tree.column('#5', anchor=CENTER, width='100')
    tree.heading('#5', text='Admin ID')
    tree.column('#6', anchor=CENTER, width='100')
    tree.heading('#6', text='Item ID')
     
    def approve_selected(selected_requests): 
        approve_info = []  
        displayItems = [] 
        for i in selected_requests: 
            requestId = tree.item(i)['values'][0] 
            itemId = tree.item(i)['values'][5] 
            approve_info.append((requestId, itemId)) 
            displayItems.append(requestId) 
        approveall = messagebox.askyesno( 
            title="Confirm Approval", message="Click Yes to confirm approval of the following requests: \n\n{}".format(displayItems)) 
        if approveall: 
            for i in range(len(approve_info)): 
                approveAndUpdateRequestStatusAndTagAdminID(approve_info[i][0], adminID, approve_info[i][1])
            messagebox.showinfo( 
                title="Requests Approved", message="Requests successfully approved. Thank you!") 
            changepage("approveHomePage", adminID)

    if table_info == []:
        messagebox.showinfo('Good news!', 'No requests waiting to be approved')
    else:
        for i in table_info:
            tree.insert("", "end", values=i)
        tkinter.Button(text="Approve Selected Requests", height="2", width="30", bg="#91d521", fg="#FFFFFF", font=(
            'Calibri', 20),  relief=tkinter.SOLID, command=lambda: approve_selected(tree.selection())).pack()

    tkinter.Label(text="", bg='#e6bbad').pack()
    tkinter.Button(text="Back To Admin Home Page", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("adminHomePage", adminID)).pack(side=tkinter.BOTTOM)
    return

def updateServiceStatus(itemID):
    updateRequestStatus = "UPDATE item SET serviceStatus = 'Completed' WHERE itemID = %s"
    mycursor.execute(updateRequestStatus % itemID)
    mydb.commit()
    return

def ServiceItemsPage(root, cursor, adminID):
    main_screen = root
    main_screen.title("OSHES app")
    main_screen.config(bg='#e6bbad')
    main_screen.grid()

    tkinter.Label(text="Here are the items currently in progress of being serviced :)",
                  width="300", height="2", font=("Calibri", 13)).pack()
    selection_statement = "SELECT itemID, serviceStatus, customerID, adminID FROM item WHERE serviceStatus = 'In progress'"
    cursor.execute(selection_statement)
    table_info = cursor.fetchall()
    cursor.reset()

    style = ttk.Style()
    style.theme_use('default')
    tree = ttk.Treeview(root, columns=('Item ID', 'Service Status',
                        'Customer ID', 'Admin ID'), show='headings')
    tree.pack()

    root.title('Service Page')
    tree.column('#1', anchor=CENTER, width='100')
    tree.heading('#1', text='Item ID')
    tree.column('#2', anchor=CENTER, width='100')
    tree.heading('#2', text='Service Status')
    tree.column('#3', anchor=CENTER, width='100')
    tree.heading('#3', text='Customer ID')
    tree.column('#4', anchor=CENTER, width='100')
    tree.heading('#4', text='Admin ID')

    def service_selected(selected_items):
        service_itemIDs = []
        for i in selected_items:
            itemId = tree.item(i)['values'][0]
            service_itemIDs.append(itemId)
        approveall = messagebox.askyesno(
            title="Confirm Service of Items?", message="Click Yes to confirm completion of services of the following items: \n\n{}".format(service_itemIDs))
        if approveall:
            for i in service_itemIDs:
                updateServiceStatus(i)
            messagebox.showinfo(
                title="Items Serviced.", message="Items successfully serviced. Thank you!")
            changepage("serviceItemsPage", adminID)

    if table_info == []:
        messagebox.showinfo('Good news!', 'No items left to service.')
    else:
        for i in table_info:
            tree.insert("", "end", values=i)
        tkinter.Button(text="Service Selected Items", height="2", width="30", bg="#91d521", fg="#FFFFFF", font=(
            'Calibri', 20),  relief=tkinter.SOLID, command=lambda: service_selected(tree.selection())).pack()

    tkinter.Label(text="", bg='#e6bbad').pack()
    tkinter.Button(text="Back To Admin Home Page", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("adminHomePage", adminID)).pack(side=tkinter.BOTTOM)
    return



def CustomerBuySearch(root, cursor, currCustomerID):
    for widget in root.winfo_children():
        widget.destroy()

    def buy_item(itemID):
        if len(itemID) != 4 or not list(items.find({"ItemID": itemID})):
            messagebox.showerror(
                title="Error", message="Please enter a valid Item ID")
        else:
            buy = messagebox.askyesno(
                message="You are buying item {}".format(itemID))
            if buy:
                if itemSold(cursor, itemID):
                    messagebox.showerror(
                        title="Out of stock", message="Item ID {} is out of stock.".format(itemID))
                else:
                    getAndUpdateItem(itemID, currCustomerID)
                    messagebox.showinfo(
                        title="Item purchased!", message="Thank you for your purchase!\nItem bought: " + itemID)

    ws = root
    ws.title('Customer - Home')
    ws.config(bg='#add8e6')
    tkinter.Label(ws, text="Welcome " + customerName + " [ID:" + str(
        currCustomerID) + "]", width="300", height="2", font=("Calibri", 13)).pack()
    tkinter.Label(ws, text="", bg='#add8e6').pack()
    tkinter.Button(ws, text="Search and Buy items", height="2", width="30",
                   relief=tkinter.SOLID, command=lambda: changepage("SearchPage", currCustomerID)).pack()
    tkinter.Label(ws, text="", bg='#add8e6').pack()
    tkinter.Label(ws, text="To buy, please enter Item ID",
                  width="300", height="2", font=("Calibri", 13)).pack()
    # for buy entry
    f = ('Times', 14)
    tkinter.Label(ws, text="Enter item ID here", bg='#CCCCCC', font=f)
    itemid = tkinter.Entry(ws, font=f)
    itemid.pack()
    tkinter.Button(ws, text="Buy", height="2", width="30",
                   relief=tkinter.SOLID, command=lambda: buy_item(itemid.get())).pack()
    tkinter.Label(ws, text="", bg='#add8e6').pack()
    tkinter.Button(text="Back to Customer Home Page", height="2", width="30", bg="#e6d8ad",
                   relief=tkinter.SOLID, command=lambda: changepage("customerHomePage", currCustomerID)).pack()
    return


def SearchPage(root, cursor, customerID):
    for widget in root.winfo_children():
        widget.destroy()
    ws = root
    ws.title('Choose a category!')
    ws.wm_geometry("1040x900")
    ws.config(bg='#add8e6')
    
    '''# Category
    categories = [default_category, "Lights", "Locks"]
    category = tkinter.StringVar()
    category.set(categories[0])
    dropcat = tkinter.OptionMenu(root, category, *categories)
    dropcat.pack()

    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Light model:", bg='#add8e6').pack()
    # Model
    lights = [default_category, "Light1", "Light2", "SmartHome1"]
    light = tkinter.StringVar()
    light.set(lights[0])
    droplight = tkinter.OptionMenu(root, light, *lights)
    droplight.pack()
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Lock model:", bg='#add8e6').pack()
    locks = [default_category, "Safe1", "Safe2", "Safe3", "SmartHome1"]
    lock = tkinter.StringVar()
    lock.set(locks[0])
    droplock = tkinter.OptionMenu(root, lock, *locks)
    droplock.pack()'''

    # Category
    tkinter.Label(text="Select Category:", bg='#add8e6').pack()
    default_category = "No option selected"

    def update_model_options(category_selected):
        menu = dropmodels['menu']
        menu.delete(0, 'end')
        if category_selected == 'Lights':
            selected_models = [default_category, 'Light1', 'Light2', 'SmartHome1']
        elif category_selected == 'Locks':
            selected_models = [default_category, 'Safe1', 'Safe2', 'Safe3', 'SmartHome1']
        else:
            selected_models = [default_category, 'Light1', 'Light2', 'Safe1', 'Safe2', 'Safe3', 'SmartHome1']
        # models.set('No option selected')
        for each_model in selected_models:
            menu.add_command(label=each_model, command=lambda x=each_model: on_model_change(x))

    category = tkinter.StringVar()
    category_choices = [default_category, 'Lights', 'Locks']
    category.set(category_choices[0])
    dropcat = tkinter.OptionMenu(root, category, *category_choices, command=update_model_options)
    # formatting: dropcat.config(bg='white', fg='black', width=15, relief=tkinter.GROOVE)
    # dropcat.place(x=130, y=110)
    dropcat.pack()
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Model:", bg='#add8e6').pack()

    # Models
    def on_model_change(model_selected):
        models.set(model_selected)

    models = tkinter.StringVar()
    model_choices = [default_category, 'Light1', 'Light2', 'Safe1', 'Safe2', 'Safe3', 'SmartHome1']
    models.set(model_choices[0])
    dropmodels = tkinter.OptionMenu(root, models, *model_choices, command=on_model_change)
    dropmodels.pack()
    #dropmodels.config(bg='white', fg='black', width=15, relief=tkinter.GROOVE)
    #dropmodels.place(x=130, y=150)


    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Advanced Filter Options:", bg='#add8e6').pack()

    # Advanced options

    # Colour

    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Color:", bg='#add8e6').pack()
    colors = [default_category, "White", "Blue",
              "Yellow", "Green", "Black"]
    color = tkinter.StringVar()
    color.set(colors[0])
    dropcolor = tkinter.OptionMenu(root, color, *colors)
    dropcolor.pack()

    # Factory
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Factory:", bg='#add8e6').pack()
    factories = [default_category, "Malaysia", "China", "Philippines"]
    factory = tkinter.StringVar()
    factory.set(factories[0])
    dropfactory = tkinter.OptionMenu(root, factory, *factories)
    dropfactory.pack()

    # Power supply
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Power Supply:", bg='#add8e6').pack()
    powersupplies = [default_category, "Battery", "USB"]
    powersupply = tkinter.StringVar()
    powersupply.set(powersupplies[0])
    droppowersupply = tkinter.OptionMenu(root, powersupply, *powersupplies)
    droppowersupply.pack()

    # Production year
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Production Year:", bg='#add8e6').pack()
    prodyears = [default_category, "2014", "2015",
                 "2016", "2017", "2018", "2019", "2020", ]
    prodyear = tkinter.StringVar()
    prodyear.set(prodyears[0])
    dropprodyear = tkinter.OptionMenu(root, prodyear, *prodyears)
    dropprodyear.pack()

    # Price
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="Select Price Range:", bg='#add8e6').pack()
    tkinter.Label(text="Min:", bg='#add8e6').pack()
    minprice = StringVar(value = '0')
    maxprice = StringVar(value = '200')
    pricemin = tkinter.Entry(textvariable=minprice)
    pricemin.pack()
    tkinter.Label(text="Max:", bg='#add8e6').pack()
    pricemax = tkinter.Entry(textvariable=maxprice)
    pricemax.pack()

    advanced_options = {
        'Color': color, 
        'Factory': factory,
        "PowerSupply": powersupply, 
        "ProductionYear": prodyear,
        "MinPrice": minprice,
        "MaxPrice": maxprice
        }

    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Label(text="", bg='#add8e6').pack()
    def areThereSearchResults():
        item_count = 0
        color = advanced_options['Color'].get()
        factory = advanced_options['Factory'].get()
        powerSupply = advanced_options['PowerSupply'].get()
        prodYear = advanced_options['ProductionYear'].get()
        find_dict = {}
        if category.get() != default_category:
            find_dict['Category'] = category.get()
        if category.get() == "Lights" and category.get() != default_category:
            find_dict['Model'] = models.get()
        if category.get() == "Locks" and category.get() != default_category:
            find_dict['Model'] = models.get()
        if color != default_category:
            find_dict['Color'] = color
        if factory != default_category:
            find_dict['Factory'] = factory
        if powerSupply != default_category:
            find_dict['PowerSupply'] = powerSupply
        if prodYear != default_category:
            find_dict['ProductionYear'] = prodYear

        for item in items.find(find_dict):
            if itemSold(cursor, item['ItemID']):
                continue
            item_count += 1

        if item_count == 0:
            return False
        return True
    tkinter.Button(text="Search", height="2", width="30", relief=tkinter.SOLID,
                   command=lambda: SimpleSearchResult(root, cursor, category.get(), (models.get() if category.get() == "Lights" else models.get()), advanced_options, customerID) 
                   ).pack()
                   ##if areThereSearchResults() else messagebox.showinfo('No search results!')
    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Button(text="Back to Buy/Search page", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: CustomerBuySearch(root, cursor, customerID)).pack(side=tkinter.TOP)
    return


def SimpleSearchResult(root, cursor, cat, mod, advanced_options, customerID):
    for widget in root.winfo_children():
        widget.destroy()
    ws = root
    ws.title('Search results')
    ws.config(bg='#add8e6')
    f = ('Calibri', 13)

    color = advanced_options['Color'].get()
    factory = advanced_options['Factory'].get()
    powerSupply = advanced_options['PowerSupply'].get()
    prodYear = advanced_options['ProductionYear'].get()
    try:
        minPrice = int(advanced_options['MinPrice'].get())
        maxPrice = int(advanced_options['MaxPrice'].get())
    except:
        messagebox.showerror(title="Invalid Price Range", message="Price range should be from 0 to 200 ($)")
        SearchPage(root, cursor, customerID)
    else:
        if (minPrice < 0 or maxPrice < 0 or minPrice > maxPrice):
            messagebox.showerror(title="Invalid Price Range", message="Price range should be from 0 to 200 ($)")
            SearchPage(root, cursor, customerID)
    
    default_category = "No option selected"
    search_string = ""
    if cat != default_category:
        search_string += "Category: " + cat + ", "
    if mod != default_category:
        search_string += "Model: " + mod + ", "
    if color != default_category:
        search_string += "Color: " + color + ", "
    if factory != default_category:
        search_string += "Factory: " + factory + ", "
    if powerSupply != default_category:
        search_string += "powerSupply: " + powerSupply + ", "
    if prodYear != default_category:
        search_string += "productionYear: " + prodYear + ", "
    search_string += "Price range: {} to {}, ".format(minPrice, maxPrice)
    tkinter.Label(text="Search results for {}".format(
        search_string[:-2]), bg='#CCCCCC', font=f).grid(row=0, column=0)

    # display search result below

    style = ttk.Style()
    style.theme_use("default")
    columns = ('ItemID', 'Category', 'Model', 'Color', 'Factory', 'PowerSupply',
               'PurchaseStatus', 'ProductionYear', 'Price', 'Warranty (months)')
    tree = ttk.Treeview(root, columns=columns, show='headings')
    for i in range(len(columns)):
        tree.column("#{}".format(i+1), anchor=CENTER,
                    minwidth=0, width=100, stretch=tkinter.NO)
        tree.heading("#{}".format(i+1), text=columns[i])

    item_count = 0
    # Creating of MongoDB query dict
    find_dict = {}
    if cat != default_category:
        find_dict['Category'] = cat
    if mod != default_category:
        find_dict['Model'] = mod
    if color != default_category:
        find_dict['Color'] = color
    if factory != default_category:
        find_dict['Factory'] = factory
    if powerSupply != default_category:
        find_dict['PowerSupply'] = powerSupply
    if prodYear != default_category:
        find_dict['ProductionYear'] = prodYear
    

    for item in items.find(find_dict):
        if itemSold(cursor, item['ItemID']):
            continue
        item_count += 1
        values = (
            item['ItemID'],
            item['Category'],
            item['Model'],
            item['Color'],
            item['Factory'],
            item['PowerSupply'],
            item['PurchaseStatus'],
            item['ProductionYear'],
            itemPriceWarrantyCost(item['Category'], item['Model'])[0],
            itemPriceWarrantyCost(item['Category'], item['Model'])[1]
        )
        price = int(values[-2])
        if price >= minPrice and price <= maxPrice:
            tree.insert("", "end", values=values)

    tree.grid(row=1, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(ws, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')

    def buy_selected(selected_items, customerID):
        buy_itemIDs = []
        for i in selected_items:
            itemId = tree.item(i)['values'][0]
            buy_itemIDs.append(itemId)

        buyall = messagebox.askyesno(
            title="Confirm Purchase", message="Click Yes to confirm purchase of the following items: \n\n{}".format(buy_itemIDs))
        if buyall:
            for i in buy_itemIDs:
                getAndUpdateItem(i, customerID)
            messagebox.showinfo(
                title="Items purchased", message="Items successfully purchased. Thank you!")
            SimpleSearchResult(root, cursor, cat, mod,
                               advanced_options, customerID)

    if item_count == 0:
        tkinter.Label(text="No items matching your search.",
                      bg='#FFFFFF').grid(row=3, column=0)
    else:
        tkinter.Label(text="Number of items in stock: " +
                      str(item_count), bg='#FFFFFF').grid(row=3, column=0)

    tkinter.Button(text="Back to search", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: SearchPage(root, cursor, customerID)).grid(row=4, column=0)
    tkinter.Button(text="Back to buy/search page", height="2", width="50", bg="#b5f09d", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: CustomerBuySearch(root, cursor, customerID)).grid(row=5, column=0)
    tkinter.Button(text="BUY SELECTED ITEMS", height="2", width="30", bg="#91d521", fg="#FFFFFF", font=(
        'Calibri', 20),  relief=tkinter.SOLID, command=lambda: buy_selected(tree.selection(), customerID)).grid(row=6, column=0)


def CustomerAllRequestsPage(root, cursor, customerID):
    root.title("Customer Request Page")
    f = ('Calibri', 13)
    tkinter.Label(text="All my Requests :)",
                  bg='#CCCCCC', font=f).grid(row=0, column=0)
    reqSQL = "SELECT requestID, requestDate, requestStatus FROM request WHERE customerID = %s"
    cursor.execute(reqSQL, (customerID,))
    req = cursor.fetchall()

    style = ttk.Style()
    style.theme_use("default")
    columns = ('requestID', 'requestDate', 'requestStatus')
    tree = ttk.Treeview(root, columns=columns, show='headings')
    for i in range(len(columns)):
        tree.column("#{}".format(i+1), anchor=CENTER,
                    minwidth=0, width=100, stretch=tkinter.NO)
        tree.heading("#{}".format(i+1), text=columns[i])

    for item in req:
        tree.insert("", "end", values=item)

    tree.grid(row=1, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(
        root, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')
    tkinter.Button(text="Back to Customer Home Page", height="2", width="30", bg="#e6d8ad",
                   relief=tkinter.SOLID, command=lambda: changepage("customerHomePage", customerID)).grid(row=3, column=0)
    return


def CustomerCancelRequestPage(root, cursor, customerID):
    root.title("Customer Request Page")
    f = ('Calibri', 13)
    tkinter.Label(text="Requests that I can cancel :)",
                  bg='#CCCCCC', font=f).grid(row=0, column=0)
    reqToCancelSQL = "SELECT requestID, requestDate, requestStatus FROM request WHERE customerID = %s\
                      AND requestStatus != 'Approved'\
                      AND requestStatus != 'Canceled'\
                      AND requestStatus != 'Completed'"
    cursor.execute(reqToCancelSQL, (customerID,))
    reqToCancel = cursor.fetchall()
    for i in range(len(reqToCancel)):
        requestID = reqToCancel[i][1]
        requestDate = reqToCancel[i][0]
        requestStatus = reqToCancel[i][2]

    style = ttk.Style()
    style.theme_use("default")
    columns = ('requestID', 'requestDate', 'requestStatus')
    tree = ttk.Treeview(root, columns=columns, show='headings')
    for i in range(len(columns)):
        tree.column("#{}".format(i+1), anchor=CENTER,
                    minwidth=0, width=150, stretch=tkinter.YES)
        tree.heading("#{}".format(i+1), text=columns[i])

    for item in reqToCancel:
        tree.insert("", "end", values=item)

    tree.grid(row=1, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(
        root, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')
    tkinter.Button(text="CANCEL SELECTED REQUESTS", height="2", width="30", bg="#91d521", fg="#FFFFFF", font=(
        'Calibri', 20),  relief=tkinter.SOLID, command=lambda: cancel_selected(tree.selection(), customerID)).grid(row=2, column=0)
    tkinter.Button(text="Back to Customer Home Page", height="2", width="30", bg="#e6d8ad",
                   relief=tkinter.SOLID, command=lambda: changepage("customerHomePage", customerID)).grid(row=3, column=0)
    
    def cancel_selected(selected_items, customerID):
        cancel_info = []
        for i in selected_items:
            requestID = tree.item(i)['values'][0]
            cancel_info.append(requestID)

        reqall = messagebox.askyesno(
            title="Confirm Request Cancellation", message="Click Yes to cancel request of the following items: \n\n{}".format(cancel_info))
        if reqall:
            for i in cancel_info:
                getAndCancelRequest(i)
                messagebox.showinfo(
                title="Requests cancelled", message="Requests have been cancelled. Thank you!")
            changepage("customerCancelRequestPage", customerID)
    return


def CustomerRequestPage(root, cursor, customerID):
    root.title("Customer Request Page")
    f = ('Calibri', 13)
    tkinter.Label(text="Items that I can make Requests for :)",
                  bg='#CCCCCC', font=f).grid(row=0, column=0)
    itemsToRequestSQL = "SELECT productID, i.itemID, dateOfPurchase FROM item i left join request re on re.itemid = i.itemid and re.customerid = i.customerid where i.customerid = %s and (servicestatus = %s and (requeststatus != 'Submitted and Waiting for payment' or requeststatus is null))"
    cursor.execute(itemsToRequestSQL, (customerID, ""))
    itemsToRequest = cursor.fetchall()
    for i in range(len(itemsToRequest)):
        itemID = itemsToRequest[i][1]
        productID = itemsToRequest[i][0]
        dateOfPurchase = itemsToRequest[i][2]
        d = list(products.find({"ProductID": productID}))[0]
        warranty = d['Warranty (months)']
        cost = d['Cost ($)']
        serviceFee = 40 + 0.2 * int(cost)
        itemsToRequest[i] = (productID, itemID, dateOfPurchase,
                             warranty, isPastWarranty(dateOfPurchase, warranty),
                             serviceFee if isPastWarranty(dateOfPurchase, warranty) else 0)

    style = ttk.Style()
    style.theme_use("default")
    columns = ('productID', 'itemID', 'dateOfPurchase',
               "Warranty (months)", 'itemPastWarranty' , 'serviceFee')
    tree = ttk.Treeview(root, columns=columns, show='headings')
    for i in range(len(columns)):
        tree.column("#{}".format(i+1), anchor=CENTER,
                    minwidth=0, width=100, stretch=tkinter.NO)
        tree.heading("#{}".format(i+1), text=columns[i])

    for item in itemsToRequest:
        tree.insert("", "end", values=item)

    tree.grid(row=1, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(
        root, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')
    tkinter.Button(text="REQUEST SELECTED ITEMS", height="2", width="30", bg="#91d521", fg="#FFFFFF", font=(
        'Calibri', 20),  relief=tkinter.SOLID, command=lambda: req_selected(tree.selection(), customerID)).grid(row=2, column=0)
    tkinter.Button(text="Back to Customer Home Page", height="2", width="30", bg="#e6d8ad",
                   relief=tkinter.SOLID, command=lambda: changepage("customerHomePage", customerID)).grid(row=3, column=0)
    
    def req_selected(selected_items, customerID):
        req_info = []
        pay = False 
        yesPay = True
        displayItems = []
        for i in selected_items:
            itemId = tree.item(i)['values'][1]
            itemPastWarranty = tree.item(i)['values'][4]
            serviceFee = tree.item(i)['values'][5]
            req_info.append((itemId, itemPastWarranty, serviceFee))
            displayItems.append(itemId)

        reqall = messagebox.askyesno(
            title="Confirm Request", message="Click Yes to confirm request of the following items: \n\n{}".format(displayItems))
        if reqall:
            for i in range(len(req_info)):
                itemPastWarranty = True if req_info[i][1] == "True" else False 
                if itemPastWarranty:
                    pay = True
                getAndRequestItem(req_info[i][0], customerID, itemPastWarranty, req_info[i][2])
            if pay:
                yesPay = messagebox.askyesno(
                    title = "Pay up!!!",
                    message = "You have chosen an item(s) which have expired warranty. This requires Payment before the Administrator can approve the Request. Continue?"
                )
            if yesPay: 
                messagebox.showinfo(
                title="Requests submitted", message="Requests for Items have been submitted. Thank you!")
            changepage("customerRequestPage", customerID)
    return


def isPastWarranty(dateOfPurchase, warranty):
    return (datetime.datetime.today().date() - dateOfPurchase).days > warranty * 30


def getAndRequestItem(itemID, customerID, itemPastWarranty, serviceFee):
    #handle cancelled request
    getReqID = "SELECT requestID from request WHERE customerID = %s AND itemID = %s"
    mycursor.execute(getReqID, (customerID, itemID))
    status = "Submitted and Waiting for payment" if itemPastWarranty else "Submitted"
    a = False 
    try: 
        a = mycursor.fetchone()[0]
    except:
        a = False 
    if not a:
        makeRequest = "INSERT INTO request (requestDate, requestStatus, customerID, adminID, itemID) VALUES (%s, %s, %s, NULL, %s)"
        mycursor.execute(makeRequest, (datetime.datetime.today().strftime('%Y-%m-%d'), status, customerID, itemID))
    else:
        reqID = a
        updateReq = "UPDATE request SET requestStatus = %s WHERE requestID = %s"
        mycursor.execute(updateReq, (status, reqID))
        updateAgain = "UPDATE request SET requestDate = %s WHERE requestID = %s"
        mycursor.execute(updateAgain, (datetime.datetime.today().strftime('%Y-%m-%d'), reqID))


    if itemPastWarranty:
        getReqID = "SELECT requestID FROM request WHERE customerID = %s AND itemID = %s"
        mycursor.execute(getReqID, (customerID, itemID))
        reqID = mycursor.fetchone()[0]
        createServiceFee = "INSERT INTO servicefee (requestID, creationDate, feeAmount) VALUES (%s, %s, %s)"
        mycursor.execute(createServiceFee, (reqID, datetime.datetime.today().strftime('%Y-%m-%d'), serviceFee))
    else: 
        updateItem = "UPDATE item SET serviceStatus = 'Waiting for approval' WHERE itemID = %s"
        mycursor.execute(updateItem, (itemID,))
    mydb.commit()

def CustomerItemsPage(root, cursor, customerID):
    sql_statement = "SELECT itemID FROM item where customerID = '%s' "
    cursor.execute(sql_statement % customerID)
    table_info = cursor.fetchall()
    cursor.reset()

    style = ttk.Style()
    style.theme_use('default')
    columns = ('ItemID', 'Category', 'Model', 'Color', 'Factory', 'PowerSupply',
               'ProductionYear', 'Price', 'Warranty (months)')
    tree = ttk.Treeview(root, columns=columns, show='headings')
    tree.pack()

    root.title('Customer Items Page')
    for i in range(len(columns)):
        tree.column("#{}".format(i+1), anchor=CENTER,
                    minwidth=0, width=100, stretch=tkinter.NO)
        tree.heading("#{}".format(i+1), text=columns[i]) 

    if table_info == []:
        messagebox.showinfo('Oh no!', 'You did not purchase any items!')
    else:
        for itemID in table_info:
            for item in items.find({"ItemID" : itemID[0]}):
                cat = item['Category']
                mod = item['Model']
                col = item['Color']
                fact = item['Factory']
                powersup = item['PowerSupply']
                prodyear = item['ProductionYear']
                price = itemPriceWarrantyCost(cat, mod)[0]
                warranty = itemPriceWarrantyCost(cat, mod)[1]
                values = (itemID[0], cat, mod, col, fact, powersup, prodyear, price, warranty)
                tree.insert("", "end", values=values)  

    tkinter.Label(text="", bg='#add8e6').pack()
    tkinter.Button(text="Back To Customer Home Page", height="2", width="30", bg="#e6d8ad", relief=tkinter.SOLID,
                   cursor='hand2', command=lambda: changepage("customerHomePage", customerID)).pack(side=tkinter.BOTTOM)
    return 

def CustomerPayRequests(root, cursor, customerID):
    # Page to view, select and pay for requests submitted by customer which requires payment
    ws = root
    ws.title('Pay for submitted requests')
    ws.config(bg='#add8e6')
    f = ('Calibri', 13)

    tkinter.Label(text="Requests you have submitted which require payment", font=f).grid(row=0, column=0)

    style = ttk.Style()
    style.theme_use("default")
    columns = ('requestID', 'requestDate', 'requestStatus', 'itemID', 'feeAmount')
    tree = ttk.Treeview(root, columns=columns, show='headings', selectmode="browse")
    for i in range(len(columns)):
        tree.column("#{}".format(i+1), anchor=CENTER,
                    minwidth=0, width=150, stretch=tkinter.NO)
        tree.heading("#{}".format(i+1), text=columns[i])

    requestsToPaySQL = (
        "SELECT r.requestID, requestDate, requestStatus, itemID, feeAmount " +
        "FROM servicefee sf LEFT JOIN request r ON sf.requestID = r.requestID " +
        "WHERE customerID = {} and requestStatus = 'Submitted and Waiting for payment'"
    ).format(customerID)
    cursor.execute(requestsToPaySQL)
    requestsToPay = cursor.fetchall()
    for r in requestsToPay:
        tree.insert("", "end", values=r)

    tree.grid(row=1, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(ws, orient=tkinter.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')


    def pay_selected(selected_items):
        requests = []
        for i in selected_items:
            item = tree.item(i)['values']
            requestID = item[0]
            itemID = item[3]
            paymentAmount = item[4]
            requests.append((requestID, itemID, paymentAmount))
        
            

        payall = messagebox.askyesno(
            title="Confirm Payment", message="Click Yes to confirm payment of the following request: \n\nRequest ID: {}".format([x[1] for x in requests]))
        if payall:
            for item in requests:
                requestID = item[0]
                itemID = item[1]
                paymentAmount = item[2]
                
                # update servicefee.settlementdate
                update_servicefee = "UPDATE servicefee SET settlementDate = %s WHERE requestID = %s"
                mycursor.execute(update_servicefee, (datetime.datetime.today().strftime('%Y-%m-%d'), requestID))
                # update request.requestStatus
                update_requeststatus = "UPDATE request SET requestStatus = %s WHERE requestID = %s"
                mycursor.execute(update_requeststatus, ("In progress", requestID))
                # update item.serviceStatus
                update_itemservicestatus = "UPDATE item SET serviceStatus = %s WHERE itemID = %s"
                mycursor.execute(update_itemservicestatus, ("Waiting for approval", itemID))
                # create payment
                createPayment = "INSERT INTO payment (customerID, requestID, paymentDate, paymentAmount) VALUES (%s, %s, %s, %s)"
                mycursor.execute(createPayment, (customerID, requestID, datetime.datetime.today().strftime('%Y-%m-%d'), paymentAmount))

                
                mydb.commit()

                
            messagebox.showinfo(
                title="Requests paid", message="Requests successfully paid. Thank you!")
            changepage('payServiceHomePage', customerID)

    tkinter.Button(text="Back to Customer Home Page", height="2", width="30", bg="#e6d8ad",
                relief=tkinter.SOLID, command=lambda: changepage("customerHomePage", customerID)).grid(row=6, column=0)
    tkinter.Button(text="PAY SELECTED REQUEST", height="2", width="30", bg="#91d521", fg="#FFFFFF", font=(
        'Calibri', 20),  relief=tkinter.SOLID, command=lambda: pay_selected(tree.selection())).grid(row=5, column=0)


def cancelInvalidRequests():
    #payment of service fees must be made within 10 days from request date 
    '''
    updateStatement = "update request re\
         right join servicefee se on (re.requestid = se.requestid)\
         set re.requestStatus = 'Canceled'\
         where (date_add(creationdate, interval 10 day) < current_date())"
    '''
    mycursor.execute("SET SQL_SAFE_UPDATES = 0")

    e = "update request re\
        set re.requestStatus = 'Canceled'\
        where (date_add(requestDate, interval 10 day) < current_date() = 1)\
        and requestStatus = 'Submitted and Waiting for payment'"

    #if service fees are not made by the due date, the request will be canceled automatically
    mycursor.execute(e)
    mycursor.execute("SET SQL_SAFE_UPDATES = 1")
    mydb.commit()
    return


def getAndCancelRequest(requestID):
    #change the serviceStatus of the item back to ""
    getItemID = "SELECT itemID from request where requestID = %s"
    mycursor.execute(getItemID, (requestID,))
    itemID = mycursor.fetchone()[0]
    updateItem = "UPDATE item SET servicestatus = %s where itemid = %s"
    mycursor.execute(updateItem, ("", itemID))
    #cancel request
    del_statement = "UPDATE request SET requestStatus = 'Canceled' where requestID = %s"
    mycursor.execute(del_statement, (requestID,))
    #delete serviceFee is any
    dele = "DELETE from servicefee where requestid = %s"
    mycursor.execute(dele, (requestID,))

    mydb.commit()

def getAndUpdateItem(itemID, customerID):
    updatePurchaseStatus = "UPDATE item SET purchaseStatus = 'Sold' WHERE itemID = %s"
    mycursor.execute(updatePurchaseStatus, (itemID,))
    updateCustomerID = "UPDATE item SET customerID = %s WHERE itemID = %s"
    mycursor.execute(updateCustomerID, (customerID, itemID))
    updateDateOfPurchase = "UPDATE item SET dateOfPurchase = %s WHERE itemID = %s"
    mycursor.execute(updateDateOfPurchase, (datetime.datetime.today().strftime('%Y-%m-%d'), itemID))
    mydb.commit()

def itemSold(cursor, itemID):
    # Returns true if item is sold (based on MYSQL item relation) and false otherwise
    return mysqlSelect("SELECT * from item WHERE itemID = '{}'".format(itemID), cursor)[0][4] == 'Sold'

def itemPriceWarrantyCost(cat, mod):
    # Returns (price, warranty) of item's category and model from mongodb products collection
    d = list(products.find({'Category': cat, 'Model': mod}))[0]
    price = d['Price ($)']
    warranty = d['Warranty (months)']
    cost = d['Cost ($)']
    return (price, warranty, cost)

def changepage(other, optional="", anotheroptional =""):
    global currpage, root
    for widget in root.winfo_children():
        widget.destroy()
    if other == "registerCustomer":
        CustomerSignUpPage(root, mycursor, mydb)
        currpage = "registerCustomer"
    elif other == "registerAdmin":
        AdminSignUpPage(root, mycursor, mydb)
        currpage = "registerAdmin"
    elif other == "loginCustomer":
        CustomerLoginPage(root, mycursor)
        currpage = "loginCustomer"
    elif other == "loginAdmin":
        AdminLoginPage(root, mycursor)
        currpage = "loginAdmin"
    elif other == "landing":
        LandingPage(root)
        currpage = "landing"
    elif other == "customerHomePage":
        CustomerHomePage(root, mycursor, optional)
        currpage = "customerHomePage"
    elif other == "adminHomePage":
        AdminHomePage(root, mycursor, optional)
        currpage = "adminHomePage"
    elif other == "approveHomePage":
        ApproveHomePage(root, mycursor, optional)
        currpage = "approveHomePage"
    elif other == "CustomerBuySearch":
        CustomerBuySearch(root, mycursor, optional)
        currpage = "CustomerBuySearch"
    elif other == "SearchPage":
        SearchPage(root, mycursor, optional)
        currpage = "SearchPage"
    elif other == "inventoryHomePage":
        InventoryHomePage(root, mycursor, optional)
    elif other == "serviceStatusesHomePage":
        ServiceStatusesPage(root, mycursor, optional)
    elif other == "serviceItemsPage":
        ServiceItemsPage(root, mycursor, optional)
    elif other == "unpaidHomePage":
        UnpaidHomePage(root, mycursor, optional)
    elif other == "customerRequestPage":
        CustomerRequestPage(root, mycursor, optional)
    elif other == "customerCancelRequestPage":
        CustomerCancelRequestPage(root, mycursor, optional)
    elif other == "customerAllRequestPage":
        CustomerAllRequestsPage(root, mycursor, optional)
    elif other == "payServiceHomePage":
        CustomerPayRequests(root, mycursor, optional)
    elif other == "adminSearchAllOrOne":
        AdminSearchAllOrOnePage(root, mycursor, optional)
        currpage = "adminSearchAllOrOne"
    elif other == "adminSearchAllPage":
        AdminSearchAllPage(root, mycursor, optional)
        currpage = "adminSearchPage"
    elif other == "adminSearchForOnePage":
        AdminSearchForOnePage(root, mycursor, optional, anotheroptional)
        currpage = "adminSearchForOnePage"
    elif other == "myItemsPage":
        CustomerItemsPage(root, mycursor, optional)
        currpage = "myItemsPage"


def executeSQL(SQLFileName, cursor):
    with open(SQLFileName, 'r') as SQLscript:
        SQLcommands = SQLscript.read().split(';')
        for command in SQLcommands:
            try:
                cursor.execute(command)
            except:
                print('Statement not executed: ' + str(command))


def mysqlSelect(command, cursor):
    # Select
    cursor.execute(command)
    result = cursor.fetchall()
    return result


# Global variables
customerName = ""
customerID = ""

# Connect MYSQL
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "s9938580d"  # your pw here since everyone got diff pw
MYSQL_DATABASE = "oshes"

mydb = mysql.connector.connect(
    host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DATABASE)
mycursor = mydb.cursor(buffered=True)

# Connect MongoDB
client = MongoClient()
mongo = client['Inventory']  # the name of your mongodb database here
items = mongo.items
products = mongo.products

# init_mysql()

currpage = "landing"
root = tkinter.Tk()
root.wm_geometry("1040x700")
LandingPage(root)
root.mainloop()