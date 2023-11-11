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
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # Create the instance of the System
        self.system = SystemValuesFunction()

        # Open image
        image_original = Image.open("background.jpg")
        resized_image = image_original.resize((size[0], size[1]))
        image_tk = ImageTk.PhotoImage(resized_image)

        # Open Logo
        my_logo = ctk.CTkImage(Image.open("Logo.png"), size=(60, 45))
        # Created the canvas
        self.canvas = BackGroundFrame(self, image_tk)

        # Create the Main Frame
        self.menuFrame = MainFrame(self)

        # Data Log frame
        self.dataFrame = DataFrame(self.menuFrame, (0, 1))

        # Create the Phases Frame
        self.phasesFrame = PhasesFrame(
            self.menuFrame, (0, 0), "PHASES FRAME", self.dataFrame
        )
        # System values Frame
        self.systemValues = SystemValues(self.menuFrame, "SYSTEM VALUES")
        # Expected Values Frame
        self.expectedFrame = ExpectedValuesFrame(
            self.menuFrame, "THEORETICAL VALUES", self.systemValues, self.system
        )
        # Results FRAME
        self.resultsFrame = ResultsFrame(self.menuFrame, "RESULTS", self.system)
        # ADD LOGO
        self.logoFrame = LogoLabel(self.menuFrame, my_logo)

        self.mainloop()


App("FLOW FOCUSING SYSTEM CALCULATOR", (800, 600))
