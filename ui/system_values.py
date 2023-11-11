from tkinter import ttk

import customtkinter as ctk


class SystemValues(ctk.CTkFrame):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.grid(row=1, column=1, rowspan=2, padx=10, pady=10)

        self.create_widgets(name)

    def create_widgets(self, name):
        # Add the label
        frame_label = ctk.CTkLabel(self, text=name)
        frame_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Add the Ca Label field
        ca_label = ctk.CTkLabel(self, text="Capillary Number: ")
        ca_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        ca_label_value = ttk.Label(self, text="---")
        ca_label_value.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Add the Surface Tension label field
        st_label = ctk.CTkLabel(self, text="Surface Tension (N/m): ")
        st_label.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        st_label_value = ttk.Label(self, text="---")
        st_label_value.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Add the Velocity Ratio label field
        vr_label = ctk.CTkLabel(self, text="Uc/Ud: ")
        vr_label.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        vr_label_value = ttk.Label(self, text="---")
        vr_label_value.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        # Add the SELECTED FLUID
        fluid_label = ttk.Label(self, text="Fluid: ")
        fluid_label.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        fluid_label_name = ttk.Label(self, text="---")
        fluid_label_name.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        # Add the CHANNEL WIDTH
        channel_label = ctk.CTkLabel(self, text="Channel width (µm): ")
        channel_label.grid(row=5, column=0, padx=5, pady=5, sticky="ew")
        channel_label_value = ttk.Label(self, text="---")
        channel_label_value.grid(row=5, column=1, padx=5, pady=5, sticky="ew")
