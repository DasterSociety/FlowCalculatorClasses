import tkinter as tk

import customtkinter as ctk


class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(corner_radius=15)
        ctk.CTkFrame(self)
        self.grid(row=0, column=0, columnspan=2, padx=60, pady=60)
        # self.pack(side="top", padx=50, pady=50)
        # self.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
