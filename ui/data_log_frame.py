import tkinter as tk
from tkinter import ttk

import openpyxl

DATA = "/Users/daster/Documents/DNT Local/OFS/Dev/FlowCalculatorClasses/DataLog.xlsx"


class DataFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=1, padx=10, pady=10)

        # Adding the scroll bar
        dataScroll = ttk.Scrollbar(self)
        dataScroll.pack(side="right", fill="y")

        # Naming the columns
        cols = ("Index", "Name", "Density", "Viscosity")
        dataTreeView = ttk.Treeview(
            self, show="headings", yscrollcommand=dataScroll.set, columns=cols, height=6
        )
        dataTreeView.column("Index", width=50)
        dataTreeView.column("Name", width=100)
        dataTreeView.column("Density", width=100)
        dataTreeView.column("Viscosity", width=100)

        dataTreeView.pack()
        dataScroll.config(command=dataTreeView.yview)

        self.loadData(dataTreeView)

        # Load the data values
        # for value_tuple in list_values[1:]:
        # dataTreeView.insert("", self.tk.END, values=value_tuple)

    def loadData(self, treeView):
        # Loading the data
        workbook = openpyxl.load_workbook(DATA)
        sheet = workbook.active
        list_values = list(sheet.values)
        print(list_values)

        # Load the Column Names
        for col_name in list_values[0]:
            treeView.heading(col_name, text=col_name)

        # Load the data values
        for value_tuple in list_values[1:]:
            treeView.insert("", tk.END, values=value_tuple)  # Load the
