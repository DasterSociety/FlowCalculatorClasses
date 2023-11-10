import tkinter as tk
from tkinter import ttk


class BackGroundFrame(ttk.Frame):
    def __init__(self, parent, imageTk):
        super().__init__(parent)

        # Set the canvas and frame
        canvas = tk.Canvas(self, bd=0, highlightthickness=0, relief="ridge")
        canvas.create_image(0, 0, image=imageTk, anchor="nw")
        canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.place(x=0, y=0, relwidth=1, relheight=1)
        # ttk.Label(self, text="ex", image=imageB).pack(expand=True, fill="both")
        # self.pack(expand=True, fill="both")
