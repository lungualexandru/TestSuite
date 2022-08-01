import tkinter as tk
import pyvisa
import numpy as np
import easy_scpi as scpi
from time import time
from tkinter import ttk
def maingui(thermo_in,chip_id,chip_descr):
    swindow = tk.Tk()
    swindow.geometry('640x480')
    tk.Button(swindow, text='Quit', command=swindow.quit).grid(row=4, column=0, sticky=tk.W, pady=4)
    tk.Button(swindow, text='Show', command=swindow.quit).grid(row=4, column=1, sticky=tk.W, pady=4)
    tk.Button(swindow, text="Done", command=swindow.quit).grid(row=4,column=3, sticky=tk.W, pady=4)

    label1=tk.Label(swindow, text="loading").grid(row=5, column=0)



    # swindow.after(1,open_ts,thermo_in,label1)
    swindow.mainloop()
    def Draw()
        global text
        frame = tk.frame(root, width=100, height=100, relief='solid',bd=1)
        frame.place(x=10, y=10)
        text=tk.Label(frame, text='Hello')
        text.pack()
    def Refresher():
        global text
        text.configure(text=time.asctime())
        root.after(1000, Refresher())
def open_ts(thermo_resource):

    dmm = scpi.Instrument(thermo_resource)
    dmm.connect()
    voltage = dmm.measure.voltage()
    return voltage
    # return tk.Label(window, text=voltage).grid(row=5, column=0)




# if __name__ == '__maingui__':
#     maingui()