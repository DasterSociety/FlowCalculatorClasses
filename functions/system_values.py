from .data import Data


class SystemValuesFunction:
    def __init__(self):
        self.ca = 0
        self.s_tension = 0
        self.vel_ratio = 0
        self.fluid_index = 0
        self.channel_width = 0
        self.qc = 0
        self.qd = 0

    def setSystemValues(self, ca, s_tension, vel_ratio, fluid_index, channel_width):
        self.ca = ca
        self.s_tension = s_tension
        self.vel_ratio = vel_ratio
        self.fluid_index = fluid_index
        self.channel_width = channel_width

    def getSystemValues(self):
        s_values = (
            self.ca,
            self.s_tension,
            self.vel_ratio,
            self.fluid_index,
            self.channel_width,
        )
        print(s_values)
        return s_values

    def CalculateFlowRateC(self):
        # ============ CALCULATIONS
        cArea = pow((self.channel_width / 1000000), 2)

        # Extract the fluid properties
        data = Data()
        viscosity = data.getViscosity(self.fluid_index)
        # Calculate Qc
        self.qc = ((self.ca * self.s_tension * cArea) / (viscosity / 1000)) * 3.6e9
        print(self.qc)
        return self.qc

    def CalculateFlowRateD(self):
        self.qd = self.qc * self.vel_ratio
        print(self.qd)
        return self.qd
