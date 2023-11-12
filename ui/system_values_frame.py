from tkinter import ttk

import customtkinter as ctk

from functions.data import Data

# from functions.system_values import SystemValuesFunction


class SystemValues(ctk.CTkFrame):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.grid(row=1, column=1, rowspan=2, padx=(5, 5), pady=10, sticky="ew")

        self.create_widgets(name)

    def create_widgets(self, name):
        # Add the label
        frame_label = ctk.CTkLabel(self, text=name, font=("Century Gothic", 16))
        frame_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Add the Ca Label field
        self.ca_label = ctk.CTkLabel(
            self, text="Capillary Number: ", font=("Century Gothic", 14)
        )
        self.ca_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.ca_label_value = ttk.Label(self, text="---")
        self.ca_label_value.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        # Add the Surface Tension label field
        self.st_label = ctk.CTkLabel(self, text="Surface Tension (N/m): ")
        self.st_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.st_label_value = ttk.Label(self, text="---")
        self.st_label_value.grid(row=2, column=1, padx=5, pady=5, sticky="e")

        # Add the Velocity Ratio label field
        self.vr_label = ctk.CTkLabel(self, text="Uc/Ud: ")
        self.vr_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.vr_label_value = ttk.Label(self, text="---")
        self.vr_label_value.grid(row=3, column=1, padx=5, pady=5, sticky="e")

        # Add the SELECTED FLUID
        self.fluid_label = ttk.Label(self, text="Fluid: ")
        self.fluid_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.fluid_label_name = ttk.Label(self, text="---")
        self.fluid_label_name.grid(row=4, column=1, padx=5, pady=5, sticky="e")

        # Add the CHANNEL WIDTH
        self.channel_label = ctk.CTkLabel(self, text="Channel width (µm): ")
        self.channel_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.channel_label_value = ttk.Label(self, text="---")
        self.channel_label_value.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    def UpdateSystemValues(self, ca, st, vr, index, cw):
        # Load DATA
        data = Data()
        name = data.getPhaseName(index)

        self.ca_label_value.config(text=str(ca))
        self.st_label_value.config(text=str(st))
        self.vr_label_value.config(text=str(vr))
        self.fluid_label_name.config(text=name)
        self.channel_label_value.config(text=str(cw))
