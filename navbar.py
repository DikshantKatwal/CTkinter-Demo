import customtkinter
from aboutus import AboutUS
from adduser import Adduser
from homescreen import HomeScreen
from settings import Settings
from datetime import datetime


class NavigationSystem:
    def __init__(self, root):
        self.root = root
        self.navbarframe = customtkinter.CTkFrame(self.root, width=200)
        self.navbarframe.pack(side='left', fill='y', padx=10,pady=10)

        button_height = 40 
        button_font=('Arial',20)
        self.fg_color='#42555C'
        self.activefg_color ='#4d5d53'

        self.timeLabel = customtkinter.CTkLabel(self.navbarframe,text="Time",height=button_height, font=('Arial',15,'bold'),width=200,corner_radius=6, fg_color="#00022e")
        self.timeLabel.grid(row=0, column=0, sticky="ew", padx=10, pady=10) 

        self.button1 = customtkinter.CTkButton(self.navbarframe, text="HomeScreen",fg_color=self.fg_color, height=button_height, font=button_font,  command=self.homescreen)
        self.button1.grid(row=1, column=0, sticky="ew", padx=10, pady=10) 

        self.button1.bind("<Button-1>", lambda event, name='HomeScreen': self.on_enter(name))
        # FOR HOVER
        # self.button1.bind("<Leave>", self.on_leave)
        # self.button1.bind("<Enter>", self.on_enter)


        self.button2 = customtkinter.CTkButton(self.navbarframe, text="About US",fg_color=self.fg_color, height=button_height, font=button_font,  command=self.aboutus)
        self.button2.grid(row=2, column=0, sticky="ew", padx=10, pady=10) 
        self.button2.bind("<Button-1>", lambda event, name='About US': self.on_enter(name))

        self.button2 = customtkinter.CTkButton(self.navbarframe, text="Settings",fg_color=self.fg_color, height=button_height, font=button_font,  command=self.settings)
        self.button2.grid(row=3, column=0, sticky="ew", padx=10, pady=10) 
        self.button2.bind("<Button-1>", lambda event, name='Settings': self.on_enter(name))

        self.button3 = customtkinter.CTkButton(self.navbarframe, text="Add User",fg_color=self.fg_color, height=button_height, font=button_font,  command=self.adduser)
        self.button3.grid(row=4, column=0, sticky="ew", padx=10, pady=10) 
        self.button3.bind("<Button-1>", lambda event, name='Add User': self.on_enter(name))


        self.button4 = customtkinter.CTkButton(self.navbarframe, text="Exit",fg_color=self.fg_color, height=button_height, font=button_font,  command=self.exit)
        self.button4.grid(row=5, column=0, sticky="ew", padx=10, pady=10) 
        self.button4.bind("<Button-1>", lambda event, name='Exit': self.on_enter(name))


        self.page_frame = customtkinter.CTkFrame(self.root)
        self.page_frame.pack(side='left', fill='both', expand=True, padx=10,pady=10)
        self.homescreen()
        self.update_time()
    
    def update_time(self):
        current_time = datetime.now().strftime("%B/%d/%Y %I:%M:%S %p")
        self.timeLabel.configure(text=f"{current_time}")
        self.root.after(1000, self.update_time) 

    def exit(self):
        self.root.destroy() 
        
    def aboutus(self):
        for widget in self.page_frame.winfo_children():
            widget.destroy()
        self.about_frame = AboutUS(self.page_frame)  

    
    def on_enter(self, button_name):
        for widget in self.navbarframe.winfo_children():
            if isinstance(widget, customtkinter.CTkButton):
                if widget.cget('text') == button_name:

                    widget.configure(fg_color=self.activefg_color)
                else:    
                    widget.configure(fg_color=self.fg_color)


    def homescreen(self):
        for widget in self.page_frame.winfo_children():
            widget.destroy()
        HomeScreen(self.page_frame)

    def settings(self):
        for widget in self.page_frame.winfo_children():
            widget.destroy()
        Settings(self.page_frame)
        
    def adduser(self):
        for widget in self.page_frame.winfo_children():
            widget.destroy()
        Adduser(self.page_frame)

