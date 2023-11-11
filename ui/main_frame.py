# from tkinter import ttk
import customtkinter as ctk


class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkFrame(self, corner_radius=15)
        self.pack(fill="none", side="top", padx=100, pady=100)
