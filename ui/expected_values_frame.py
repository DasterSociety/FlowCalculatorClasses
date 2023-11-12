# from tkinter import ttk
import customtkinter as ctk

from functions.data import Data

# from functions.system_values import SystemValuesFunction


class ExpectedValuesFrame(ctk.CTkFrame):
    def __init__(self, parent, name, frameI, system):
        super().__init__(parent)
        self.grid(row=1, column=0, rowspan=2, padx=30, pady=10, sticky="w")

        self.create_widgets(name, frameI, system)

    def create_widgets(self, name, frameI, system):
        # Add the label
        frame_label = ctk.CTkLabel(self, text=name, font=("Century Gothic", 16))
        frame_label.grid(row=0, column=0, padx=(10, 10), pady=10, sticky="ew")

        # Add the Capillary Number Entry field
        self.ca_entry = ctk.CTkEntry(
            self, border_color="#005f99", font=("Century Gothic", 14)
        )
        self.ca_entry.insert(0, "Capillary Number")
        self.ca_entry.bind("<FocusIn>", lambda e: self.ca_entry.delete("0", "end"))
        self.ca_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # Add the Surface Tension Entry field
        self.surface_entry = ctk.CTkEntry(
            self, border_color="#005f99", font=("Century Gothic", 14)
        )
        self.surface_entry.insert(0, "Surface Tension (N/m)")
        self.surface_entry.bind(
            "<FocusIn>", lambda e: self.surface_entry.delete("0", "end")
        )
        self.surface_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        # Add the Velocity Ratio Entry field
        self.vel_ratio_entry = ctk.CTkEntry(
            self, border_color="#005f99", font=("Century Gothic", 14)
        )
        self.vel_ratio_entry.insert(0, "Uc/Ud")
        self.vel_ratio_entry.bind(
            "<FocusIn>", lambda e: self.vel_ratio_entry.delete("0", "end")
        )
        self.vel_ratio_entry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        # Select the Fluid Index
        self.fluid_index_entry = ctk.CTkEntry(
            self, border_color="#005f99", font=("Century Gothic", 14)
        )
        self.fluid_index_entry.insert(0, "Fluid INDEX")
        self.fluid_index_entry.bind(
            "<FocusIn>", lambda e: self.fluid_index_entry.delete("0", "end")
        )
        self.fluid_index_entry.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

        # Entry uChannel width
        self.channel_width_entry = ctk.CTkEntry(
            self, border_color="#005f99", font=("Century Gothic", 14)
        )
        self.channel_width_entry.insert(0, "Channel width (µm)")
        self.channel_width_entry.bind(
            "<FocusIn>", lambda e: self.channel_width_entry.delete("0", "end")
        )
        self.channel_width_entry.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

        # Add the SET/CALCULATE button
        set_button = ctk.CTkButton(
            self,
            text="SET",
            font=("Century Gothic", 14),
            command=lambda: self.SetValues(frameI, system),
        )
        set_button.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

    def SetValues(self, frameI, system):
        # =============== GET INSERTED VALUES ===========
        # Read the value of the name of the phase
        ca_e = float(self.ca_entry.get())
        st_e = float(self.surface_entry.get())
        vr_e = float(self.vel_ratio_entry.get())
        index = int(self.fluid_index_entry.get())
        cw_e = float(self.channel_width_entry.get())

        # Update system data

        system.setSystemValues(ca_e, st_e, vr_e, index, cw_e)
        system.getSystemValues()

        frameI.UpdateSystemValues(ca_e, st_e, vr_e, index, cw_e)

        # # Load DATA
        # data = Data()
        # data.getPhaseName(index)

        # Update fields
        self.ca_entry.delete(0, "end")
        self.ca_entry.insert(0, "Capillary Number")

        self.surface_entry.delete(0, "end")
        self.surface_entry.insert(0, "Surface Tension (N/m)")

        self.vel_ratio_entry.delete(0, "end")
        self.vel_ratio_entry.insert(0, "Uc/Ud")

        self.fluid_index_entry.delete(0, "end")
        self.fluid_index_entry.insert(0, "Fluid INDEX")

        self.channel_width_entry.delete(0, "end")
        self.channel_width_entry.insert(0, "Channel width (µm)")
        # print(name, density, viscosity)
