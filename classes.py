# import tkinter as tk
# from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

from ui import (
    BackGroundFrame,
    DataFrame,
    ExpectedValuesFrame,
    MainFrame,
    PhasesFrame,
    ResultsFrame,
    SystemValues,
)


class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        # style = ttk.Style(self)
        # self.tk.call("source", "forest-dark.tcl")
        # style.theme_use("forest-dark")
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
        self.phasesFrame = PhasesFrame(self.menuFrame, "PHASES FRAME")
        # Expected Values Frame
        self.expectedFrame = ExpectedValuesFrame(self.menuFrame, "THEORETICAL VALUES")
        # Data Log frame
        self.dataFrame = DataFrame(self.menuFrame)
        # System values Frame
        self.systemValues = SystemValues(self.menuFrame, "SYSTEM VALUES")
        # Results FRAME
        self.resultsFrame = ResultsFrame(self.menuFrame, "RESULTS")

        self.mainloop()


App("Droplet Generator Calculator ctk", (900, 700))
