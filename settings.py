import customtkinter as ctk
import mysql.connector


class Settings:
    def __init__(self, root):
        self.root = root
        width = 250
        
        self.label = ctk.CTkLabel(self.root, text="Settings", font=('',20))
        self.label.grid(row=0, column=1, sticky="w", padx=10, pady=20)

        self.lname = ctk.CTkLabel(self.root, text='')
        self.lname.grid(row=1, column=1, sticky="w")

        self.lname = ctk.CTkLabel(self.root, text="USERNAME")
        self.lname.grid(row=2, column=0, sticky="w", padx=10, pady=10)

        self.ename = ctk.CTkEntry(self.root, width=width)
        self.ename.grid(row=2, column=1, sticky="w", padx=10, pady=10) 

        self.lcontact = ctk.CTkLabel(self.root, text="Contact Number")
        self.lcontact.grid(row=3, column=0, sticky="w", padx=10, pady=10)

        self.econtact = ctk.CTkEntry(self.root, width=width)
        self.econtact.grid(row=3, column=1, sticky="w", padx=10, pady=10) 

        self.lcompanyname = ctk.CTkLabel(self.root, text="Name of the Company")
        self.lcompanyname.grid(row=4, column=0, sticky="w", padx=10, pady=10)

        self.ecompanyname = ctk.CTkEntry(self.root, width=width)
        self.ecompanyname.grid(row=4, column=1, sticky="w", padx=10, pady=10) 

        self.lcompanyaddress = ctk.CTkLabel(self.root, text="Company Address")
        self.lcompanyaddress.grid(row=5, column=0, sticky="w", padx=10, pady=10)

        self.ecompanyaddress = ctk.CTkEntry(self.root, width=width)
        self.ecompanyaddress.grid(row=5, column=1, sticky="w", padx=10, pady=10) 

        self.lmessage = ctk.CTkLabel(self.root, text="", text_color='green',font=('',15, 'bold'))
        self.lmessage.grid(row=6, column=1, sticky="w", padx=10)
        

        savebtn = ctk.CTkButton(self.root, text='Save', command=self.save_to_database)
        savebtn.grid(row=7, column=1, sticky="w", padx=10, pady=10) 
        self.retrieve_settings()

    def retrieve_settings(self):
        conn = mysql.connector.connect(host="localhost",
                                        username="root", 
                                        password="admin", 
                                        database="db_test")
        my_cursor = conn.cursor()
        sample_id = 1
        select_query = "SELECT username, contact_number, company_name, company_address FROM settings WHERE id = %s"
        try:
        # Execute the SQL command
            my_cursor.execute(select_query, (sample_id,))

            # Fetch one row
            row = my_cursor.fetchone()
            if row:
                # Assign values to variables
                username, contact_number, company_name, company_address = row
                self.ename.insert(0, username)
                self.econtact.insert(0, contact_number)
                self.ecompanyname.insert(0, company_name)
                self.ecompanyaddress.insert(0, company_address)
            else:
                print("No data found for the provided ID.")
            conn.commit()
            conn.close()

        except Exception as e:
            print(f"Error: {e}")

    def save_to_database(self):
        conn = mysql.connector.connect(host="localhost",
                                        username="root", 
                                        password="admin", 
                                        database="db_test")
        my_cursor = conn.cursor()
        
        print(my_cursor)
        # Get data from GUI elements
        id=1
        username = self.ename.get()
        contact_number = self.econtact.get()
        company_name = self.ecompanyname.get()
        company_address = self.ecompanyaddress.get()

        # SQL query to insert data into the table
        insert_update_query = """
        INSERT INTO settings (id, username, contact_number, company_name, company_address)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        username = VALUES(username),
        contact_number = VALUES(contact_number),
        company_name = VALUES(company_name),
        company_address = VALUES(company_address)
        """

        data = (id, username, contact_number, company_name, company_address)  # Ensure six elements in the tuple

        try:
            # Execute the SQL command
            my_cursor.execute(insert_update_query, data)
            print("Data saved successfully!")
            self.lmessage.configure(text="SAVED!!!")
            self.root.after(3000,self.clear_message)
        except Exception as e:
            print(f"Error: {e}")
            # Rollback in case of an error
            conn.rollback()
        conn.commit()
        conn.close()

    def clear_message(self):
        print('hello')
        self.lmessage.configure(text="")
