import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from ui import MainFrame, PhasesFrame


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

        ## Create the Phases Frame
        self.phasesFrame = PhasesFrame(self.menuFrame, "Phases Frame")
        # self.frame = Frame(self, image_tk)
        self.mainloop()


class BackGroundFrame(ttk.Frame):
    def __init__(self, parent, imageTK):
        super().__init__(parent)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0, relief="ridge")
        canvas.create_image(0, 0, image=imageTK, anchor="nw")
        canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.place(x=0, y=0, relwidth=1, relheight=1)
        # ttk.Label(self, text="ex", image=imageB).pack(expand=True, fill="both")
        # self.pack(expand=True, fill="both")


# class MainFrame(ttk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.pack(fill="none", side="top", padx=100, pady=100)


# class PhasesFrame(ttk.LabelFrame):
#     def __init__(self, parent, name):
#         super().__init__(parent)
#         self.config(text=name)
#         ttk.LabelFrame(self, text=name)
#         self.grid(row=0, column=0, padx=10, pady=10)

#         self.create_widgets()
#         # name_entry = ttk.Entry(self)
#         # name_entry.insert(0, "Name")
#         # name_entry.bind("<FocusIn>", lambda e: name_entry.delete("0", "end"))
#         # name_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

#     def create_widgets(self):
#         # Add and Entry field
#         name_entry = ttk.Entry(self)
#         name_entry.insert(0, "Name")
#         name_entry.bind("<FocusIn>", lambda e: name_entry.delete("0", "end"))
#         name_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

#         # Add the Density field
#         density_entry = ttk.Entry(self)
#         density_entry.insert(0, "Density (kg/m^3)")
#         density_entry.bind("<FocusIn>", lambda e: density_entry.delete("0", "end"))
#         density_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

#         # Add the Viscosity field
#         viscosity_entry = ttk.Entry(self)
#         viscosity_entry.insert(0, "Viscosity (mPa * s)")
#         viscosity_entry.bind("<FocusIn>", lambda e: viscosity_entry.delete("0", "end"))
#         viscosity_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

#         # Add the Insert button
#         insert_button = ttk.Button(self, text="Insert", style="Accent.TButton")
#         insert_button.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

App("Droplet Generator Calculator", (700, 700))
