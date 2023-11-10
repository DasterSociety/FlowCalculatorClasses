import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from ui import BackGroundFrame, DataFrame, ExpectedValuesFrame, MainFrame, PhasesFrame


class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        style = ttk.Style(self)
        self.tk.call("source", "forest-dark.tcl")
        style.theme_use("forest-dark")
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # Open image
        image_original = Image.open("background.jpg")
        resized_image = image_original.resize((size[0], size[1]))
        image_tk = ImageTk.PhotoImage(resized_image)

        # Created the canvas
        self.canvas = BackGroundFrame(self, image_tk)

        # Create the Main Frame
        self.menuFrame = MainFrame(self)

        # Create the Phases Frame
        self.phasesFrame = PhasesFrame(self.menuFrame, "Phases Frame")
        # Expected Values Frame
        self.expectedFrame = ExpectedValuesFrame(self.menuFrame, "Expected Values")
        # Data Log frame
        self.dataFrame = DataFrame(self.menuFrame)

        self.mainloop()


App("Droplet Generator Calculator", (800, 800))
