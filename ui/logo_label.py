# from tkinter import ttk
import customtkinter as ctk


class LogoLabel(ctk.CTkLabel):
    def __init__(self, parent, pos, pad, j, logoTk):
        super().__init__(parent)
        self.configure(image=logoTk, text="", bg_color="transparent")
        self.grid(row=pos[0], column=pos[1], sticky=j, padx=pad[0], pady=pad[1])
