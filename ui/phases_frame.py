# from tkinter import ttk
import customtkinter as ctk


class PhasesFrame(ctk.CTkFrame):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.grid(row=0, column=0, padx=10, pady=10)

        self.create_widgets(text)
        # name_entry = ttk.Entry(self)
        # name_entry.insert(0, "Name")
        # name_entry.bind("<FocusIn>", lambda e: name_entry.delete("0", "end"))
        # name_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    def create_widgets(self, textI):
        # Add the label
        frame_lable = ctk.CTkLabel(self, text=textI)
        frame_lable.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        # Add and Entry field
        name_entry = ctk.CTkEntry(self)
        name_entry.insert(0, "Name")
        name_entry.bind("<FocusIn>", lambda e: name_entry.delete("0", "end"))
        name_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # # Add the Density field
        density_entry = ctk.CTkEntry(self)
        density_entry.insert(0, "Density (kg/m^3)")
        density_entry.bind("<FocusIn>", lambda e: density_entry.delete("0", "end"))
        density_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        # Add the Viscosity field
        viscosity_entry = ctk.CTkEntry(self)
        viscosity_entry.insert(0, "Viscosity (mPa * s)")
        viscosity_entry.bind("<FocusIn>", lambda e: viscosity_entry.delete("0", "end"))
        viscosity_entry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        # Add the Insert button
        insert_button = ctk.CTkButton(self, text="Insert")
        insert_button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
