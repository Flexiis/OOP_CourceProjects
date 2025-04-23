import csv
from tkinter import *
from tkinter import messagebox


class Interface(Tk):
    def __init__(self):
        Tk.__init__(self)

    def startGUI(self):
        print("Starting GUI main loop")
        self.mainloop()
        print("GUI main loop finished")

    def createGUI(self, width=400, height=110):
        self.simulate = 0
        # set title for the created window
        self.title("Client")
        # Input End time
        self.ImpEndtime = Entry(self, width=15)
        self.ImpEndtime.grid(column=1, row=0, padx=(5, 5), pady=(5, 5))
        self.lblEndtime = Label(self, anchor="w", width=15, text="End Time")
        self.lblEndtime.grid(column=0, row=0, padx=(5, 5), pady=(5, 5))
        # Input Delta time
        self.ImpDeltatime = Entry(self, width=15)
        self.ImpDeltatime.grid(column=1, row=1, padx=(5, 5), pady=(5, 5))
        self.lblDeltatime = Label(self, anchor="w", width=15, text="Delta Time")
        self.lblDeltatime.grid(column=0, row=1, padx=(5, 5), pady=(5, 5))
        # Input Voltage
        self.ImpVoltage = Entry(self, width=15)
        self.ImpVoltage.grid(column=1, row=2, padx=(5, 5), pady=(5, 5))
        self.lblVoltage = Label(self, anchor="w", width=15, text="Voltage")
        self.lblVoltage.grid(column=0, row=2, padx=(5, 5), pady=(5, 5))
        # Button Simulate
        self.ButSimulate = Button(self, text='Simulate', foreground="green", width=20,
                                  command=self.SimulateButtonClicked)
        self.ButSimulate.grid(column=2, row=0, padx=(5, 5), pady=(5, 5))
        # Button Motor settings
        self.ButSettings = Button(self, text='Settings Applied', foreground="blue", width=20,
                                  command=self.SettingsButtonClicked)
        self.ButSettings.grid(column=2, row=1, padx=(5, 5), pady=(5, 5))

        buffer = "%dx%d" % (int(width), int(height))
        self.geometry(buffer)
        return

    def SimulateButtonClicked(self):
        # Button Save settings
        self.ButSave = Button(self, text='Save', foreground="red", width=20, command=self.SaveButtonClicked)
        self.ButSave.grid(column=2, row=2, padx=(5, 5), pady=(5, 5))
        global simulate
        Voltage = self.ImpVoltage.get()
        Deltatime = self.ImpDeltatime.get()
        Endtime = self.ImpEndtime.get()
        StringTestList = [Voltage, Deltatime, Endtime]
        self.testStrValue(StringTestList)

    def testStrValue(self, StringTestList):
        SimulationList = []
        for element in range(len(StringTestList)):
            try:
                val = float(StringTestList[element])
                SimulationList.append(val)
            except ValueError:
                buffer = "%s cannot be converted to float" % (StringTestList[element])
                messagebox.showerror("Error", buffer)
                return
        f = open("Ready_to_simulate.txt", "w")
        f.write(str(SimulationList))
        return

    def SettingsButtonClicked(self):
        pass

    def SaveButtonClicked(self):
        writer = csv.writer(open("SimulateVal.csv", "w", newline=""))
        #        writer.writerow(Time, V, I, Tm, Alpha, w, Vbemf)
        pass

    def main(self):
        start = Interface()
        start.createGUI()
        start.startGUI()
        pass
