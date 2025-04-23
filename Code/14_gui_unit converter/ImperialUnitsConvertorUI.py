from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from UnitsConvertor import UnitsConvertor

class GraphicalUserInterface (Tk):
          def __init__(self):
              Tk.__init__(self)
              self.converter = UnitsConvertor
              print("GraphicalUserInterface: initialized")

          def startGUI(self):
              print("Starting GUI main loop")
              self.mainloop()
              print("GUI main loop finished")

          def createGUI(self, width = 500, height = 75):
              # set title for the created window
              self.title("Imperial and SI units convertor")
              # LABEL FOR IMPERIAL UNITS
              # align it to the WEST (right)
              self.lblImpUnit = Label(self, anchor="w", width=15, text="Imperial Unit")
              self.lblImpUnit.grid(column=0, row=0, padx=(5, 5), pady=(5, 5))
              self.lblImpUnit = Label(self, anchor="w", width=15, text="SI Unit")
              self.lblImpUnit.grid(column=0, row=1, padx=(5, 5), pady=(5, 5))
              self.lblImpUnit = Label(self, anchor="w", width=15, text="Select conversion")
              self.lblImpUnit.grid(column=2, row=0, padx=(5, 5), pady=(5, 5))
              #input 1
              self.impUnitIn = Entry(self, width=15)
              self.impUnitIn.grid(column=1, row=0, padx=(5, 5), pady=(5, 5))
              #input 2
              self.siUnitIn = Entry(self, width=15)
              self.siUnitIn.grid(column=1, row=1, padx=(5, 5), pady=(5, 5))
              #Conversionbox
              self.conversionChoices = Combobox(self, width=20)
              self.conversionChoices['values'] = ("no choice ", "inches to meters", "miles to meters", "fahrenheit to celsius", "pounds to kilogram")
              self.conversionChoices.grid(column=3, row=0, padx=(5, 5), pady=(5, 5))
              #Button
              self.convertButton = Button(self, text='Convert', foreground="blue", width=20, command=self.convertButtonClicked)
              self.convertButton.grid(column=3, row=1, padx=(5, 5), pady=(5, 5))

              buffer = "%dx%d" % (int(width), int(height))
              self.geometry(buffer)
              return

          def convertButtonClicked(self):
              Choice = self.conversionChoices.get()
              inputNumber = self.impUnitIn.get()
              valOk, val = self.testStrValue(inputNumber)
              self.converter()

              if "no choice" in Choice:
                  self.converter.showFailure(self.converter)

              if (valOk):
                  if "inches to meters" in Choice:
                      result = self.converter.convertInchesToMeters(self.converter, val)
                  elif "miles to meters" in Choice:
                      result = self.converter.convertMilesToMeters(self.converter, val)
                  elif "pounds to kilogram" in Choice:
                      result = self.converter.convertPoundsToKilograms(self.converter, val)
                  elif "fahrenheit to celsius" in Choice:
                      result = self.converter.convertFahrenheitToCelsius(self.converter, val)

                  self.siUnitIn.delete(0, END)
                  self.siUnitIn.insert(END, result)


          def testStrValue(self, inputNumber):
              valOk = True
              val = 0.0
              try:
                  val = float(inputNumber)
              except ValueError:
                  buffer = "%s cannot be converted to float" % (inputNumber)
                  messagebox.showerror("Error", buffer)
                  valOk = False
              return valOk, val



def main():
    converter = GraphicalUserInterface()
    converter.createGUI()
    converter.startGUI()
    converter.convertButtonClicked()
    converter.convert()
    pass


if __name__ == "__main__":
        main()
