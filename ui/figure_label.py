# from tkinter import ttk
import customtkinter as ctk


class FigureLabel(ctk.CTkLabel):
    def __init__(self, parent, pos, pad, j, logoTk):
        super().__init__(parent)
        self.configure(image=logoTk, text="")
        self.grid(
            row=pos[0], column=pos[1], columnspan=2, sticky=j, padx=pad[0], pady=pad[1]
        )
