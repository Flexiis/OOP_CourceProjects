import sympy


class ElectronicsModel():
    def __init__(self):
        pass

    def getCurrent(self, Vbemf):
        # Calculates the current at the time
        I = 0
        I = -(L * (sympy.diff(I)) + V - Vbemf) / R
        return I

    def getElecromagneticTorque(self, I):
        Tem = Kt * I
        return Tem

    def getBemf(self):
        Vbemf = Kt * w
        return Vbemf

    def main(self):
        start = ElectronicsModel()
        start.getCurrent()
        start.getBemf()
        start.getElecromagneticTorque()