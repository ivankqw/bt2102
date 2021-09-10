import tkinter

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

def CustomerSignUpPage():
    #sign up as a customer 
    ##attributes: customerId, name, gender, email, phone, address, password 
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

LoginPage()
