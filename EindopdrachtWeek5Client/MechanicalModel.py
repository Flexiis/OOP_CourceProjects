from ElectronicsModel import ElectronicsModel


class MechanicalModel():
    def __init__(self):
        I = ElectronicsModel.getCurrent()
        Tem = ElectronicsModel.getElecromagneticTorque()
        pass

    def getAngularAcceleration(self, Tem):
        Tm = Tem
        Alpha = -((B * w) - Tl + Tm) / J
        return Alpha