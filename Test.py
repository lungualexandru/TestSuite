import time
import pyvisa
import numpy as np
from matplotlib import pyplot as plt



def get_voltage_and_current(rawData):
    data = []
    voltagearr = []
    currentarr = []
    for i in range(0, len(rawData), 2):
        voltage = float(rawData[i])
        current = float(rawData[i + 1])
        voltagearr.append(voltage)
        currentarr.append(current)
    print(voltagearr)
    print(currentarr)
    return([voltagearr,currentarr])

def sweep_type(function):
    return 'F{},1X'.format(function)


def sweep_param(start, steps, step, range, delay):
    return 'Q1,{},{},{},{},{}X'.format(start, steps, step, range, delay)


rm = pyvisa.ResourceManager()
listOfIntruments = rm.list_resources()
print("The following instruments are available", listOfIntruments)

instrument = input('what instrument do you want to use :')
print('You opted to use ', instrument)
isInputValid = instrument in listOfIntruments
print("the instrument you picked ", isInputValid)
querylist = ""
if isInputValid:
    inst = rm.open_resource(instrument)
    inst.write(sweep_type(0))
    inst.write(sweep_param(0, 5, 2, 2, 500))
    inst.write("N1X")
    inst.write("H0X")
    time.sleep(5)
    inst.write("G5,1,2X")
    querylist = (inst.query("Measure$")).replace("NSSWV", "").replace("NMSWI", "").split(",")
else:
    print("the instrument you picked was not found")
graphData = get_voltage_and_current(querylist)
for item in graphData:
     print(item)
plt.title("Voltage Sweep")
plt.xlabel("Voltage")
plt.ylabel("Current")
plt.plot(graphData);
plt.show()
