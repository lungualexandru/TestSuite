import time
import pyvisa
import numpy as np
from matplotlib import pyplot as plt

rm = pyvisa.ResourceManager()
rm.list_resources()
inst = rm.open_resource('GPIB0::22::INSTR')
inst.write("F0,1X")
inst.write("Q1,0,5,1,2,100X")
inst.write("N1X")
inst.write("H0X")
time.sleep(5)
inst.write("G5,1,2X")
querylist = (inst.query("Measure$")).replace("NSSWV", "").replace("NMSWI", "").split(",")


def get_voltage_and_current(rawData):
    data = []
    for i in range(0, len(querylist), 2):
        voltage = float(querylist[i])
        current = float(querylist[i + 1])
        sweep = [voltage, current]
        data + sweep
    return data


graphData = get_voltage_and_current(querylist)
for item in graphData:
    print(item)

plt.title("Voltage Sweep")
plt.xlabel("Voltage")
plt.ylabel("Current")
plt.plot(querylist);
plt.show()
