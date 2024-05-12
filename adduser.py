import customtkinter as ctk
import mysql.connector
import hashlib

class Adduser:
    def __init__(self, root=None):
        self.root = root
        width = 250
        
        self.label = ctk.CTkLabel(self.root, text="Add User", font=('',20))
        self.label.grid(row=0, column=1, sticky="w", padx=10, pady=20)

        self.lname = ctk.CTkLabel(self.root, text='')
        self.lname.grid(row=1, column=1, sticky="w")

        self.lname = ctk.CTkLabel(self.root, text="Username")
        self.lname.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        self.ename = ctk.CTkEntry(self.root, width=width)
        self.ename.grid(row=2, column=1, sticky="w", padx=10, pady=10) 

        self.lpassword = ctk.CTkLabel(self.root, text="Password")
        self.lpassword.grid(row=3, column=0, sticky="w", padx=10, pady=10)

        self.epassword = ctk.CTkEntry(self.root, width=width)
        self.epassword.grid(row=3, column=1, sticky="w", padx=10, pady=10) 

        self.lrepassword = ctk.CTkLabel(self.root, text="Re-Password")
        self.lrepassword.grid(row=4, column=0, sticky="w", padx=10, pady=10)

        self.erepassword = ctk.CTkEntry(self.root, width=width)
        self.erepassword.grid(row=4, column=1, sticky="w", padx=10, pady=10) 


        self.lmessage = ctk.CTkLabel(self.root, text="", text_color='green',font=('',15, 'bold'))
        self.lmessage.grid(row=5, column=1, sticky="w", padx=10)
        

        savebtn = ctk.CTkButton(self.root, text='Save user', command=self.saveuser)
        savebtn.grid(row=6, column=1, sticky="w", padx=10, pady=10) 


    def saveuser(self):

        username = self.ename.get()
        password = self.epassword.get()
        re_password = self.erepassword.get()

        if password == re_password and username:
            conn = mysql.connector.connect(host="localhost",
                                        username="root", 
                                        password="admin", 
                                        database="db_test")
            my_cursor = conn.cursor()

            hashed_password = self.hash_password(password)
            insert_query = "INSERT INTO auth_users (username, password) VALUES (%s, %s)"
            user_data = (username, hashed_password)

            my_cursor.execute(insert_query, user_data)
            conn.commit()
            conn.close()

        else:
            self.lmessage.configure(text="Password Did'nt Match",text_color='red')
            self.root.after(3000,self.clear_message)

        

    def clear_message(self):
        self.lmessage.configure(text="")
        
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
   