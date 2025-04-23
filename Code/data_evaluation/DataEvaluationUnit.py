import csv


lst1 = []
lsttimeMIN = []
lsttimeMAX = []
lstvalMAX = ()
lstvalMIN = ()
time = []
value = []
lstMA = []
lstRTS = []


def readSignalAcquisitionData(lst1):
    f = open("lab03A_inputData.csv", "r")
    lst1 = list(csv.reader(f, delimiter=','))
    for element in (lst1[1:]):
        time.append(float(element[0]))
        value.append(float(element[1]))
    print("Time table: ", time)
    print("Value table: ", value)


def getSignalMaxList():
    global lstvalMAX
    lstvalMAX = float(max(value))
    for element in range(len(value)):
        if value[element] == lstvalMAX:
            timeMAX = time[element]
            lsttimeMAX.append(timeMAX)
    print("Maximum value:       ",lstvalMAX)
    print("Maximum value times: ",lsttimeMAX)
    return lstvalMAX


def getSignalMinList():
    global lstvalMIN
    lstvalMIN = float(min(value))
    for element in range(len(value)):
        if value[element] == lstvalMIN:
            timeMIN = time[element]
            lsttimeMIN.append(timeMIN)
    print("Minimum value:       ", lstvalMIN)
    print("Minimum value times: ", lsttimeMIN)
    return lstvalMIN


def findSignalAmplitude():
    amplitude = (abs(max(value)) + abs(min(value)))
    print("Amplitude: ", amplitude)


def filterSignalData_MA(value):
    n = 3

    for i in range(len(value) - 2):
        noemer = value[i] + value[i + 1] + value[i + 2]
        teller = n
        yi = noemer/teller
        lstMA.append(yi)
        RTS = time[i+2]
        lstRTS.append(RTS)
    f = open("lab03A_smoothenedData.csv", "w")
    for i in range(len(lstRTS)):
        f.write("{}, {}\n".format(lstRTS[i], lstMA[i]))


def main(value, lst1):
    readSignalAcquisitionData(lst1)
    getSignalMaxList()
    getSignalMinList()
    findSignalAmplitude()
    filterSignalData_MA(value)


main(value, lst1)