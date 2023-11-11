import openpyxl

DATA = "DataLog.xlsx"


class Data:
    def __init__(self):
        self.workbook = openpyxl.load_workbook(DATA)
        self.sheet = self.workbook.active
        self.data = list(self.sheet.values)

    def getData(self):
        # print(self.data)
        return self.data

    def addData(self, new_data):
        list_values = self.data
        last_index = int(list_values[-1][0]) + 1
        data_index = (last_index,) + new_data
        print(new_data)
        print(data_index)
        self.sheet.append(data_index)
        self.workbook.save(DATA)
        self.data = list(self.sheet.values)
        return data_index

    def getPhaseName(self, index):
        e_data = list(self.sheet.values)
        fluid_name = e_data[index][1]
        # Set the fluid name
        print(fluid_name)
        return fluid_name

    def getViscosity(self, index):
        e_data = list(self.sheet.values)
        print(index)
        viscosity = float(e_data[index][3])
        # Set the fluid name
        print(viscosity)
        return viscosity
