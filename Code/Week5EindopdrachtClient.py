from tkinter import *
import math
import socket

class Client:
    def ClientStart(self):
        print("*************************")
        print("*   C H A T     A P P   *")
        print("*     C L I E N T       *")
        print("*************************")
        HOST = '127.0.0.1'
        PORT = 65431
        dataToSend = ()
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((HOST, PORT))
        print("connection done... %s" % (str(clientSocket)))
        while(not("quit" in dataToSend)):
            dataToSend = input("input data ")
            print("sending data...")
            clientSocket.send(dataToSend.encode('utf-8'))
        clientSocket.close()


class Interface(Tk):
    def __init__(self):
        Tk.__init__(self)
        print("GraphicalUserInterface: initialized")

    def startGUI(self):
        print("Starting GUI main loop")
        self.mainloop()
        print("GUI main loop finished")

    def createGUI(self, width=400, height=200):
        # set title for the created window
        self.title("Eindopdracht Client")
        # Button
        self.convertButton = Button(self, text='Simulate', foreground="black", width=20, command=self.convertButtonClicked)
        self.convertButton.grid(column=1, row=1, padx=(5, 5), pady=(5, 5))

        buffer = "%dx%d" % (int(width), int(height))
        self.geometry(buffer)
        return

    def convertButtonClicked(self):
        pass
    
"""
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

class MechanicalModel():
    def __init__(self):
        I = ElectronicsModel.getCurrent()
        Tem = ElectronicsModel.getElecromagneticTorque()
        pass

    def getAngularAcceleration(self, Tem):
        Tem = Tm
        Alpha = -((B * w) - Tl + Tm) / J
        return Alpha

"""
def main():
    client = Client()
    client.ClientStart()
    interface = Interface()
    interface.startGUI()
    interface.createGUI()

    pass

if __name__ == "__main__":
        main()