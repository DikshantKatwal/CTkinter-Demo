import customtkinter
import signup, homescreen,aboutus



# self.root.geometry("1550x800+0+0")
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()



if __name__== "__main__":
    # add authentication !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    root=customtkinter.CTk()
    obj=signup.SignUP(root)
    root.mainloop()