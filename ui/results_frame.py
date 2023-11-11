from tkinter import ttk

import customtkinter as ctk


class ResultsFrame(ctk.CTkFrame):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.configure(border_width=2, border_color="green")
        self.grid(row=1, column=2, padx=10, pady=10)

        self.create_widgets(name)

    def create_widgets(self, name):
        # Add the label
        frame_label = ctk.CTkLabel(self, text=name)
        frame_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Add the Qc Results Label fields
        qc_label = ctk.CTkLabel(self, text="Qc (ml/h): ")
        qc_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        qc_label_value = ttk.Label(self, text="-----")
        qc_label_value.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Add the Qd Results Label fields
        qd_label = ctk.CTkLabel(self, text="Qd (ml/h): ")
        qd_label.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        qd_label_value = ttk.Label(self, text="-----")
        qd_label_value.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Add the CALCULATE button
        calculate_button = ctk.CTkButton(self, text="CALCULATE")
        calculate_button.grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew"
        )
