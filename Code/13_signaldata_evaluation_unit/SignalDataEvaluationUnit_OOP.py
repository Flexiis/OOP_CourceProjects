import csv


class SignalDataIOUnit:
    def __init__(self):
        self.timeList = []
        self.valuesList = []
        pass

    def readSignalAcquisitionData(self, fileName):
        timeList = self.timeList
        valuesList = self.valuesList

        f = open(fileName, "r")
        lst1 = list(csv.reader(f, delimiter=','))
        for element in (lst1[1:]):
            timeList.append(float(element[0]))
            valuesList.append(float(element[1]))
        print("Time table: ", timeList)
        print("Value table: ", valuesList)
        return timeList, valuesList

    def writeFilteredData(self, fileName, lstMA, lstRTS):
        #lstRTS = self.lstRTS
        #lstMA = self.lstMA
        with open(fileName, 'w') as csvfile:
            fileName_writer = csv.writer(csvfile, delimiter=',')
            fileName_writer.writerows([lstRTS])
            fileName_writer.writerows([lstMA])
        #f = open(fileName, "w")
        #for i in range(len(lstRTS)):
        #    f.write("{}, {}\n".format(lstRTS[i], lstMA[i]))


class SignalDataProcessingUnit:
    def __init__(self):
        self.lstvalMAX = ()
        self.lstvalMIN = ()
        self.timeList = []
        self.valuesList = []

    def getSignalMaxList(self):
        valuesList = self.valuesList
        timeList = self.timeList
        lsttimeMAX = []

        lstvalMAX = float(max(valuesList))
        for element in range(len(valuesList)):
            if valuesList[element] == lstvalMAX:
                timeMAX = timeList[element]
                lsttimeMAX.append(timeMAX)
        print("Maximum value:       ", lstvalMAX)
        print("Maximum value times: ", lsttimeMAX)
        return lstvalMAX, lsttimeMAX

    def getSignalMinList(self):
        valuesList = self.valuesList
        timeList = self.timeList
        lsttimeMIN = []

        lstvalMIN = float(min(valuesList))
        for element in range(len(valuesList)):
            if valuesList[element] == lstvalMIN:
                timeMIN = timeList[element]
                lsttimeMIN.append(timeMIN)
        print("Minimum value:       ", lstvalMIN)
        print("Minimum value times: ", lsttimeMIN)
        return lstvalMIN, lsttimeMIN

    def findSignalAmplitude(self, mn, mx):
        amplitude = (abs(mx - mn))
        print("Amplitude: ", amplitude)
        return amplitude

    def filterSignalData_MA(self, n):
        valuesList = self.valuesList
        timeList = self.timeList

        lstMA = []
        time = ()
        lstRTS = []
        for i in range(len(valuesList) - (n-1)):
            noemer = sum(valuesList[i: i + n])
            teller = n
            yi = noemer / teller
            lstMA.append(yi)
            RTS = timeList[i + (n-1)]
            lstRTS.append(RTS)
        return lstMA, lstRTS


def main():
    dataIO = SignalDataIOUnit()
    dataProcessing = SignalDataProcessingUnit()
    dataProcessing.timeList, dataProcessing.valuesList = dataIO.readSignalAcquisitionData("lab03B_inputData.csv")
    lstvalMAX, lsttimeMAX = dataProcessing.getSignalMaxList()
    lstvalMIN, lsttimeMIN = dataProcessing.getSignalMinList()
    amplitude = dataProcessing.findSignalAmplitude(lstvalMIN, lstvalMAX)
    print(lstvalMAX, lstvalMIN, amplitude)
    lstMA, lstRTS = dataProcessing.filterSignalData_MA(7)
    dataIO.writeFilteredData("lab03B_smoothenedData.csv", lstMA, lstRTS)

main()