from tkinter import ttk


class PhasesFrame(ttk.LabelFrame):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.config(text=name)
        ttk.LabelFrame(self, text=name)
        self.grid(row=0, column=0, padx=10, pady=10)

        self.create_widgets()
        # name_entry = ttk.Entry(self)
        # name_entry.insert(0, "Name")
        # name_entry.bind("<FocusIn>", lambda e: name_entry.delete("0", "end"))
        # name_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    def create_widgets(self):
        # Add and Entry field
        name_entry = ttk.Entry(self)
        name_entry.insert(0, "Name")
        name_entry.bind("<FocusIn>", lambda e: name_entry.delete("0", "end"))
        name_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # Add the Density field
        density_entry = ttk.Entry(self)
        density_entry.insert(0, "Density (kg/m^3)")
        density_entry.bind("<FocusIn>", lambda e: density_entry.delete("0", "end"))
        density_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # Add the Viscosity field
        viscosity_entry = ttk.Entry(self)
        viscosity_entry.insert(0, "Viscosity (mPa * s)")
        viscosity_entry.bind("<FocusIn>", lambda e: viscosity_entry.delete("0", "end"))
        viscosity_entry.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        # Add the Insert button
        insert_button = ttk.Button(self, text="Insert", style="Accent.TButton")
        insert_button.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
