import tkinter as tk

import customtkinter as ctk
import openpyxl

from functions.data import Data

from .data_log_frame import DataFrame

DATA = "/Users/daster/Documents/DNT Local/OFS/Dev/FlowCalculatorClasses/DataLog.xlsx"


class PhasesFrame(ctk.CTkFrame):
    def __init__(self, parent, pos, text, frameI):
        self.root = super().__init__(parent)
        self.grid(row=pos[0], column=pos[1], padx=10, pady=10)

        self.create_widgets(text, frameI)
        # name_entry = ttk.Entry(self)
        # name_entry.insert(0, "Name")
        # name_entry.bind("<FocusIn>", lambda e: name_entry.delete("0", "end"))
        # name_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    def create_widgets(self, textI, frameI):
        # Add the label
        frame_label = ctk.CTkLabel(self, text=textI)
        frame_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # Add and Entry field
        self.name_entry = ctk.CTkEntry(self, border_color="#005f99")
        self.name_entry.insert(0, "Name")
        self.name_entry.bind("<FocusIn>", lambda e: self.name_entry.delete("0", "end"))
        self.name_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # # Add the Density field
        self.density_entry = ctk.CTkEntry(self, border_color="#005f99")
        self.density_entry.insert(0, "Density (kg/m^3)")
        self.density_entry.bind(
            "<FocusIn>", lambda e: self.density_entry.delete("0", "end")
        )
        self.density_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        # Add the Viscosity field
        self.viscosity_entry = ctk.CTkEntry(self, border_color="#005f99")
        self.viscosity_entry.insert(0, "Viscosity (mPa * s)")
        self.viscosity_entry.bind(
            "<FocusIn>", lambda e: self.viscosity_entry.delete("0", "end")
        )
        self.viscosity_entry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        # Add the Insert button
        insert_button = ctk.CTkButton(
            self, text="Insert", command=lambda: self.InsertRow(frameI)
        )
        insert_button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

    def InsertRow(self, frame):
        # =============== GET INSERTED VALUES ===========
        # Read the value of the name of the phase
        name = self.name_entry.get()
        # Read the Density value
        density = float(self.density_entry.get())
        # Read the Viscosity value
        viscosity = float(self.viscosity_entry.get())
        # Verify entries
        new_data = (name, density, viscosity)
        # print(name, density, viscosity)

        # =============== INSERT VALUES TO EXCEL ===========
        #
        data = Data()
        index_data = data.addData(new_data)
        print(index_data)

        # =============== UPDATE TREEVIEW FRAME ===========
        frame.addNewData(index_data)

        #  # =============== CLEAR UI VALUES ===============
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, "Name")

        self.density_entry.delete(0, "end")
        self.density_entry.insert(0, "Density (kg/m^3)")

        self.viscosity_entry.delete(0, "end")
        self.viscosity_entry.insert(0, "Viscosity (mPa * s)")
        # print(name, viscosity, density)
