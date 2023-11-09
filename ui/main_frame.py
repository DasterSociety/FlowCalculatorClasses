from tkinter import ttk


class MainFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="none", side="top", padx=100, pady=100)
