import tkinter as tk
from tkinter import ttk

import customtkinter as ctk

from functions.data import Data


class DataFrame(ctk.CTkFrame):
    def __init__(self, parent, pos):
        super().__init__(parent)
        self.grid(row=pos[0], column=pos[1], columnspan=2, padx=10, pady=10)

        self.createWidgets()

        # dataScroll.config(command=dataTreeView.yview)

        # Load the data values
        # for value_tuple in list_values[1:]:
        # dataTreeView.insert("", self.tk.END, values=value_tuple)

    def createWidgets(self):
        # Adding the scroll bar
        dataScroll = ttk.Scrollbar(self)
        dataScroll.pack(side="right", fill="y")

        # Naming the columns
        cols = ("Index", "Name", "Density", "Viscosity")
        self.dataTreeView = ttk.Treeview(
            self, show="headings", yscrollcommand=dataScroll.set, columns=cols, height=6
        )

        self.dataTreeView.column("Index", width=80)
        self.dataTreeView.column("Name", width=200)
        self.dataTreeView.column("Density", width=100)
        self.dataTreeView.column("Viscosity", width=100)

        self.dataTreeView.pack()

        dataFrame = Data()
        self.loadDataToTreeView(dataFrame.getData(), self.dataTreeView)

    def loadDataToTreeView(self, data, treeViewI):
        # Load HEADINGS
        for col_name in data[0]:
            treeViewI.heading(col_name, text=col_name)

        # Load the data values
        for value_tuple in data[1:]:
            treeViewI.insert("", tk.END, values=value_tuple)

    def addNewData(self, new_tree_data):
        self.dataTreeView.insert("", tk.END, values=new_tree_data)
        print("ADDING DATA")

    def getFrame(self):
        return self
