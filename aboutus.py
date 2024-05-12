import customtkinter as ctk

class AboutUS:
    def __init__(self, root):
        self.root = root
        self.label = ctk.CTkLabel(self.root, text="Entry Value Will Appear Here")
        self.label.pack(pady=10)



