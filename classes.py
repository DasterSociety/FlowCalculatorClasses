import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        style = ttk.Style(self)
        style.theme_use
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(600, 600)

        self.mainloop()


App("Droplet Generator Calculator", (600, 600))
