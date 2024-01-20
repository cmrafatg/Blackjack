import tkinter as tk
from tkinter import messagebox
import hashlib

global username

def username_page1():
    global username
    return username


def logged_in():
    return flag

def read_file(file_details):
    file = None
    try:
        file = open(file_details, "r")
        lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("File not found")
    except Exception:
        print("Error reading from file")
    finally:
        if file:
            file.close()

def check_details(userid):
    file_details = "user_data.txt"
    read_lines = read_file(file_details)

    if read_lines is not None:
        for line in read_lines:
            details = line.split(",")
            details = [detail.strip() for detail in details]
            if details[0] == userid :
                messagebox.showinfo("Signup Failed", "Username Already Taken")
                return True
    return False

def check_details_login(userid,password):
    global username
    file_details = "user_data.txt"
    read_lines = read_file(file_details)

    if read_lines is not None:
        for line in read_lines:
            details = line.split(",")
            details = [detail.strip() for detail in details]
            if details[0] == userid and details[1]==hash_password(password):
                username = details[0]

                return True
    return False
def signup(userid, password):
    if not check_details(userid):
        file_details = "user_data.txt"
        with open(file_details, "a") as file:
            file.write(userid + "," + hash_password(password) + "\n")

def hash_password(password):
    # Hash a password using SHA-256 function
    password_bytes = password.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password_bytes)
    return sha256_hash.hexdigest()


def login(userid, password):
    if check_details_login(userid, password):
        global flag
        flag=True
        messagebox.showinfo("Login Successful", "Welcome, User")
        parent.destroy()

    else:
        messagebox.showerror("Login Failed", "Invalid username or password")






def validate_signup(userid,password,password2):
    if len(password) < 8:
        messagebox.showinfo("Signup Failed", "Password Requirements not met, too short")
    elif  len(userid) <= 5:
        messagebox.showinfo("Signup Failed", "Username Requirements not met, too short")
    elif password != password2 or password2 != password:
        messagebox.showinfo("Signup Failed", "Password do not match")
    elif check_details(userid) == False:
        signup(userid,password)
        messagebox.showinfo("Signup Successful", "Go to Login")




def login_screen():
    # Create the main window
    global username
    global parent
    parent = tk.Tk()
    parent.title("Login Form")
    parent.minsize(500, 500)

    # Create and place the username label and entry
    username_label = tk.Label(parent, text="Username:")
    username_label.pack()

    username_entry = tk.Entry(parent)
    username_entry.pack()
    username = username_entry.get()

    # Create and place the password label and entry
    password_label = tk.Label(parent, text="Password:")
    password_label.pack()

    password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
    password_entry.pack()

    # Create and place the login button
    login_button = tk.Button(parent, text="Login", command=lambda: login(username_entry.get(), password_entry.get()))
    login_button.pack()

    signup_button = tk.Button(parent, text="Signup", command=signup_screen)
    signup_button.pack()

    # Start the Tkinter event loop
    parent.mainloop()






def signup_screen():
    # Create the main window
    parent = tk.Tk()
    parent.title("Signup Form")
    parent.minsize(500, 500)

    # Create and place the username label and entry
    username_label = tk.Label(parent, text="Username: (Must have a length of at least 5 characters)")
    username_label.pack()

    username_entry = tk.Entry(parent)
    username_entry.pack()

    # Create and place the password label and entry
    password_label = tk.Label(parent, text="Password: (Must have a length of at least 8 characters)")
    password_label.pack()

    password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
    password_entry.pack()


    # Create and place the password label and entry
    re_password_label = tk.Label(parent, text="Password Again:")
    re_password_label.pack()

    re_password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
    re_password_entry.pack()

    # Create and place the signup button
    signup_button = tk.Button(parent, text="Signup", command=lambda :validate_signup(username_entry.get(),password_entry.get(),re_password_entry.get()))
    signup_button.pack()

    # Start the Tkinter event loop
    parent.mainloop()



global flag
flag=False
# Call the login screen function

login_screen()
