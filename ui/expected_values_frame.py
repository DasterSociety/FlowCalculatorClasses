# from tkinter import ttk
import customtkinter as ctk


class ExpectedValuesFrame(ctk.CTkFrame):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.grid(row=1, column=0, padx=10, pady=10)

        self.create_widgets(name)

    def create_widgets(self, name):
        # Add the label
        frame_label = ctk.CTkLabel(self, text=name)
        frame_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # Add the Capillary Number Entry field
        ca_entry = ctk.CTkEntry(self, border_color="#005f99")
        ca_entry.insert(0, "Capillary Number")
        ca_entry.bind("<FocusIn>", lambda e: ca_entry.delete("0", "end"))
        ca_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # Add the Surface Tension Entry field
        surface_entry = ctk.CTkEntry(self, border_color="#005f99")
        surface_entry.insert(0, "Surface Tension (N/m)")
        surface_entry.bind("<FocusIn>", lambda e: surface_entry.delete("0", "end"))
        surface_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        # Add the Velocity Ratio Entry field
        vel_ratio_entry = ctk.CTkEntry(self, border_color="#005f99")
        vel_ratio_entry.insert(0, "Uc/Ud")
        vel_ratio_entry.bind("<FocusIn>", lambda e: vel_ratio_entry.delete("0", "end"))
        vel_ratio_entry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        # Select the Fluid Index
        fluid_index_entry = ctk.CTkEntry(self, border_color="#005f99")
        fluid_index_entry.insert(0, "Fluid INDEX")
        fluid_index_entry.bind(
            "<FocusIn>", lambda e: fluid_index_entry.delete("0", "end")
        )
        fluid_index_entry.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

        # Entry uChannel width
        channel_width_entry = ctk.CTkEntry(self, border_color="#005f99")
        channel_width_entry.insert(0, "Channel width (µm)")
        channel_width_entry.bind(
            "<FocusIn>", lambda e: channel_width_entry.delete("0", "end")
        )
        channel_width_entry.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

        # Add the SET/CALCULATE button
        set_button = ctk.CTkButton(self, text="SET")
        set_button.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
