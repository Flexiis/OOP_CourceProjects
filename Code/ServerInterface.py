class Interface (Tk):
    def __init__(self):
        Tk.__init__(self)
        print("GraphicalUserInterface: initialized")

    def startGUI(self):
        print("Starting GUI main loop")
        self.mainloop()
        print("GUI main loop finished")

    def createGUI(self, width=400, height=200):
        # set title for the created window
        self.title("Eindopdracht Server")
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
        # Output value
        self.OutVal = Entry(self, width=15)
        self.OutVal.grid(column=2, row=2, padx=(5, 5), pady=(5, 5))
        self.lblVal = Label(self, anchor="w", width=15, text="End Value")
        self.lblVal.grid(column=2, row=1, padx=(5, 5), pady=(5, 5))
        # Button
        self.convertButton = Button(self, text='Input Values', foreground="black", width=20, command=self.convertButtonClicked)
        self.convertButton.grid(column=2, row=0, padx=(5, 5), pady=(5, 5))

        buffer = "%dx%d" % (int(width), int(height))
        self.geometry(buffer)
        return

    def convertButtonClicked(self):
        pass