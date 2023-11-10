from tkinter import ttk


class ExpectedValuesFrame(ttk.LabelFrame):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.config(text=name)
        ttk.LabelFrame(self, text=name)
        self.grid(row=1, column=0, padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        # Add the Capillary Number Entry field
        ca_entry = ttk.Entry(self)
        ca_entry.insert(0, "Capillary Number")
        ca_entry.bind("<FocusIn>", lambda e: ca_entry.delete("0", "end"))
        ca_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # Add the Surface Tension Entry field
        surface_entry = ttk.Entry(self)
        surface_entry.insert(0, "Surface Tension (N/m)")
        surface_entry.bind("<FocusIn>", lambda e: surface_entry.delete("0", "end"))
        surface_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # Add the Velocity Ratio Entry field
        vel_ratio_entry = ttk.Entry(self)
        vel_ratio_entry.insert(0, "Uc/Ud")
        vel_ratio_entry.bind("<FocusIn>", lambda e: vel_ratio_entry.delete("0", "end"))
        vel_ratio_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        # Select the Fluid Index
        fluid_index_entry = ttk.Entry(self)
        fluid_index_entry.insert(0, "Fluid INDEX")
        fluid_index_entry.bind(
            "<FocusIn>", lambda e: fluid_index_entry.delete("0", "end")
        )
        fluid_index_entry.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        # Entry uChannel width
        channel_width_entry = ttk.Entry(self)
        channel_width_entry.insert(0, "Channel width (µm)")
        channel_width_entry.bind(
            "<FocusIn>", lambda e: channel_width_entry.delete("0", "end")
        )
        channel_width_entry.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

        # Add the SET/CALCULATE button
        set_button = ttk.Button(self, text="SET", style="Accent.TButton")
        set_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
