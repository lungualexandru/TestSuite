import tkinter as tk
import pyvisa
import numpy as np
import easy_scpi as scpi
from time import time
from tkinter import ttk


def maingui(thermo_in, chip_id, chip_descr):
    swindow = tk.Tk()
    swindow.geometry('640x480')
    tk.Button(swindow, text='Quit', command=swindow.quit).grid(row=4, column=0, sticky=tk.W, pady=4)
    tk.Button(swindow, text='Show', command=swindow.quit).grid(row=4, column=1, sticky=tk.W, pady=4)
    tk.Button(swindow, text="Done", command=swindow.quit).grid(row=4, column=3, sticky=tk.W, pady=4)

    meas_voltage = open_ts(thermo_in)
    volts_arr = []
    def update_voltage():
        vlt = measure_volts(meas_voltage)
        swindow.after(1000, update_voltage)
        volts_arr.append(float(vlt))
        print("volts", volts_arr)
        tk.Label(swindow, text="Current measured voltage is: {}".format(vlt)).grid(row=5, column=0)
        return volts_arr

    update_voltage()
    swindow.mainloop()


def measure_volts(inst):
    return inst.measure.voltage()


def open_ts(thermo_resource):
    dmm = scpi.Instrument(thermo_resource)
    dmm.connect()
    return dmm
