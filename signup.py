import customtkinter as ctk
import tkinter as tk
from navbar import NavigationSystem

from adduser import Adduser
import mysql.connector


class SignUP:
    def __init__(self, root):
        self.root = root
        root.geometry("1000x700")
        root.overrideredirect(True) 
        
        root.title("My application")
        
        self.signupLabel = ctk.CTkLabel(self.root,font=('Arial',25,'bold'), text="Sign Up")
        self.signupLabel.place(relx=0.5, rely=0.2, anchor='center')

        self.username = ctk.CTkEntry(self.root, width=200,height=30, placeholder_text="USERNAME" )
        self.username.place(relx=0.5, rely=0.3, anchor='center')

        self.password = ctk.CTkEntry(self.root,height=30, width=200, placeholder_text='PASSWORD', show="*")
        self.password.place(relx=0.5, rely=0.37, anchor='center')

        self.message = ctk.CTkLabel(self.root,font=('Arial',13), text="", text_color="red")
        self.message.place(relx=0.5, rely=0.41, anchor='center') 
        
        signup_btn = ctk.CTkButton(self.root, text='Sign Up', command=self.authentication)
        signup_btn.place(relx=0.5, rely=0.46, anchor='center')

        exit = ctk.CTkButton(self.root, text='Exit',fg_color='red', command=self.exit)
        exit.place(relx=0.9, rely=0.05, anchor='center')

    def exit(self):
        self.root.destroy()  
    def authentication(self):
        username = self.username.get()
        password = self.password.get()
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="db_test"
            )
            my_cursor = conn.cursor()
            select_query = "SELECT password FROM auth_users WHERE username = %s"
            my_cursor.execute(select_query, (username,))
            row = my_cursor.fetchone()
            if row:
                hashed_password_db = row[0]
                user = Adduser.hash_password(self, password)
                
                hashed_password_input = user

                if hashed_password_db == hashed_password_input:
                    print("Authentication successful")
                    return self.navigationsystem()
                else:
                    self.message.configure(text="Incorrect Password ;(")
                    self.root.after(3000,self.clear_message)
            else:
                self.message.configure(text="User Not Found ;(")
                self.root.after(3000,self.clear_message)
        except mysql.connector.Error as error:
            print(f"Error during authentication: {error}")

        finally:
            my_cursor.close()
            conn.close() 

  
    def navigationsystem(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        NavigationSystem(self.root)

    def clear_message(self):
        self.message.configure(text="")

