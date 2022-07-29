import pyvisa
import time
import numpy as np
from matplotlib import pyplot as plt

def sweep_type(function):
    return 'F{},1X'.format(function)


def sweep_param(start, steps, step, range, delay):
    return 'Q1,{},{},{},{},{}X'.format(start, steps, step, range, delay)


def trigger_run(instance, sleeptime):
    instance.write("N1X")
    instance.write("H0X")
    time.sleep(sleeptime)


def get_data(data):
    data.write("G5,1,2X")
    formatted_data = data.query("Measure$").replace("NSSWV", "").replace("NMSWI", "").split(",")
    return formatted_data


def get_sleep_time(swpstr):
    sweepdelay = swpstr.split(",")[5].replace("X", "")
    sweepsteps = swpstr.split(",")[2].replace("x", "")
    sleeptime = int(sweepdelay) * int(sweepsteps)
    return sleeptime / 1000

# def plot_data(rawdata):
    # plt.title("Voltage Sweep")
    # plt.xlabel("Voltage")
    # plt.ylabel("Current")
    # ypoints = rawdata[1::2]
    # xpoints = rawdata[0::2]
    # yint = [float(x) for x in ypoints]
    # xint = [float(y) for y in xpoints]
    # plt.plot(xint, yint)
    # plt.show()
    # return (xint, yint)

def main():
    rm = pyvisa.ResourceManager()
    rm.list_resources()
    myinstr = rm.open_resource('GPIB0::22::INSTR')
    myinstr.write(sweep_type(0))
    sweepstr = sweep_param(0, 8, 0.2, 2, 50)
    myinstr.write(sweepstr)
    trigger_run(myinstr, get_sleep_time(sweepstr))
    pltdata = get_data(myinstr)
    # plot_data(pltdata)
    rm.close()
    return pltdata


if __name__ == '__main__':
    main()















































































































































