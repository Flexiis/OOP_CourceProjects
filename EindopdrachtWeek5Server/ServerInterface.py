from tkinter import *
from tkinter import messagebox
from ServerStart import Server


class Interface (Tk):
    def __init__(self):
        Tk.__init__(self)
        self.server = Server()

    def startGUI(self):
        print("Starting GUI main loop")
        self.mainloop()
        print("GUI main loop finished")

    def createGUI(self, width=400, height=200):
        # set title for the created window
        self.title("Server")
        # align it to the WEST (right)
        # input Inductance
        self.ImpInductance = Entry(self, width=15)
        self.ImpInductance.grid(column=1, row=0, padx=(5, 5), pady=(5, 5))
        self.lblInductance = Label(self, anchor="w", width=15, text="Inductance")
        self.lblInductance.grid(column=0, row=0, padx=(5, 5), pady=(5, 5))
        # input Resistance
        self.ImpResistance = Entry(self, width=15)
        self.ImpResistance.grid(column=1, row=1, padx=(5, 5), pady=(5, 5))
        self.lblResistance = Label(self, anchor="w", width=15, text="Resistance")
        self.lblResistance.grid(column=0, row=1, padx=(5, 5), pady=(5, 5))
        # input Torque (Load)
        self.ImpTorque = Entry(self, width=15)
        self.ImpTorque.grid(column=1, row=2, padx=(5, 5), pady=(5, 5))
        self.lblTorque = Label(self, anchor="w", width=15, text="Torque")
        self.lblTorque.grid(column=0, row=2, padx=(5, 5), pady=(5, 5))
        # input Motor inertia
        self.ImpMotorinertia = Entry(self, width=15)
        self.ImpMotorinertia.grid(column=1, row=3, padx=(5, 5), pady=(5, 5))
        self.lblMotorinertia = Label(self, anchor="w", width=15, text="Motor Inertia")
        self.lblMotorinertia.grid(column=0, row=3, padx=(5, 5), pady=(5, 5))
        # input Motor’s viscosity friction
        self.ImpFriction = Entry(self, width=15)
        self.ImpFriction.grid(column=1, row=4, padx=(5, 5), pady=(5, 5))
        self.lblFriction = Label(self, anchor="w", width=15, text="Friction")
        self.lblFriction.grid(column=0, row=4, padx=(5, 5), pady=(5, 5))
        # input Motor constant
        self.ImpConstant = Entry(self, width=15)
        self.ImpConstant.grid(column=1, row=5, padx=(5, 5), pady=(5, 5))
        self.lblConstant = Label(self, anchor="w", width=15, text="Constant")
        self.lblConstant.grid(column=0, row=5, padx=(5, 5), pady=(5, 5))
        # Button
        self.SendButton = Button(self, text='Input Values', foreground="white", background="black", width=20, height=11, command=self.SendButtonClicked)
        self.SendButton.place(y=5, x=250)

        buffer = "%dx%d" % (int(width), int(height))
        self.geometry(buffer)


    def SendButtonClicked(self):
        Inductance = self.ImpInductance.get()
        Resistance = self.ImpResistance.get()
        Constant = self.ImpConstant.get()
        Torque = self.ImpTorque.get()
        Friction = self.ImpFriction.get()
        Motorinertia = self.ImpMotorinertia.get()

        StringTestList = [Inductance, Resistance, Torque, Motorinertia, Friction, Constant]
        self.testStrValue(StringTestList)
        self.server.SendData()
        return StringTestList

    def testStrValue(self, StringTestList):
        MotorValuesList = []
        for element in range(len(StringTestList)):
            try:
                val = float(StringTestList[element])
                MotorValuesList.append(val)
            except ValueError:
                messagebox.showerror("Error: s cannot be converted to float")

        f = open("MotorValuesString.txt", "w")
        f.write(str(MotorValuesList))
        return MotorValuesList

    def main(self):
        interface = Interface()
        interface.createGUI()
        interface.startGUI()
        pass