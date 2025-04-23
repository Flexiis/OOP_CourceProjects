from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


class UnitsConvertor:
    def __init__(self):

        pass

    def convert(self, conversionFactor):
        if "inches to meters" in Choice:
            self.convertInchesToMeters()
        elif "miles to meters" in Choice:
            self.convertMilesToMeters()
        elif "pounds to kilogram" in Choice:
            self.convertPoundsToKilograms()
        elif "fahrenheit to celsius" in Choice:
            self.convertFahrenheitToCelsius()



    def convertInchesToMeters(self, val):
        # determine conversion result as a string
        conversionFactor = 0.0254
        Meters = val * conversionFactor
        self.result = "%15.6f" % (Meters)
        return self.result

    def convertMilesToMeters(self, val):
        conversionFactor = 1609.34
        Meters = val * conversionFactor
        self.result = "%15.6f" % (Meters)
        return self.result

    def convertPoundsToKilograms(self, val):
        conversionFactor = 0.453592
        Kilos = val * conversionFactor
        self.result = "%15.6f" % (Kilos)
        return self.result

    def convertFahrenheitToCelsius(self, val):
        celsiusDegrees = (val - 32.0) * 5.0 / 9.0
        self.result = "%15.6f" % (celsiusDegrees)
        return self.result

    def showFailure(self):
        print("show message box: error")
        # message box display
        messagebox.showerror("Error", "no conversion selected")


def main():
    conversion = UnitsConvertor()
    conversion.convert()


if __name__ == "__main__":
        main()
