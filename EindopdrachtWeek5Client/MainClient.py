from ClientStart import Client
from ClientInterface import Interface
from ElectronicsModel import ElectronicsModel
from MechanicalModel import MechanicalModel
import threading


def main():
    threading.Thread(target=Client().main).start()
    threading.Thread(target=Interface().main).start()

#    threading.Thread(target=ElectronicsModel().ElectronicsModel).start()
#    ElectronicsModel().ElectronicsModel()
#    MechanicalModel().MechanicalModel()
    pass

if __name__ == "__main__":
        main()