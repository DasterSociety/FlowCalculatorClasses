# import tkinter as tk
# from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

from functions.system_values import SystemValuesFunction

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

from ui import (
    BackGroundFrame,
    DataFrame,
    ExpectedValuesFrame,
    FigureLabel,
    LogoLabel,
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
        # self.wm_attributes("-transparentcolor", "blue")
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # Create the instance of the System
        self.system = SystemValuesFunction()

        # Open image
        image_original = Image.open("background.jpg")
        resized_image = image_original.resize((size[0], size[1]))
        image_tk = ImageTk.PhotoImage(resized_image)

        # Open Logo
        my_logo = ctk.CTkImage(Image.open("Logo.png"), size=(80, 65))

        # Open Figure
        fig = ctk.CTkImage(Image.open("FFS.png"), size=(350, 190))

        # Created the canvas
        self.canvas = BackGroundFrame(self, image_tk)

        # Create the Main Frame
        # self.menuFrame = MainFrame(self)

        # Data Log frame
        self.dataFrame = DataFrame(self, (0, 1))

        # Create the Phases Frame
        self.phasesFrame = PhasesFrame(
            self, (0, 0), "Insert Fluid Properties", self.dataFrame
        )
        # System values Frame
        self.systemValues = SystemValues(self, "Current System")
        # Expected Values Frame
        self.expectedFrame = ExpectedValuesFrame(
            self, "Set Constant Values", self.systemValues, self.system
        )
        # Results FRAME
        self.resultsFrame = ResultsFrame(self, "RESULTS", self.system)
        # ADD LOGO
        self.logoFrame = LogoLabel(self, (3, 2), (10, 10), "es", my_logo)

        self.figureFrame = FigureLabel(self, (3, 0), (100, (5, 10)), "sw", fig)

        self.mainloop()


App("FLOW-FOCUSING SYSTEM CALCULATOR", (750, 740))
