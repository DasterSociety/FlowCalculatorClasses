# from tkinter import ttk
import customtkinter as ctk


class LogoLabel(ctk.CTkLabel):
    def __init__(self, parent, logoTk):
        super().__init__(parent)
        self.configure(image=logoTk, text="")
        self.grid(row=2, column=2, sticky="e", padx=20, pady=5)
