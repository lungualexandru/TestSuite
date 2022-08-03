import tkinter as tk
import pyvisa
import numpy as np
from maingui import maingui

from tkinter import ttk


# TODO: add chip/ test subject info fields
# FIXME: fields are misaligned
# FIXME: save button should be disabled if the form is invalid
# TODO: save form to specified path
def show_entry_fields():
    print("Serial #: %s\nDescription: %s" % (e1.get(), e2.get()))


master = tk.Tk()
serial_num = tk.StringVar()
chip_descr = tk.StringVar()
target_curr = tk.DoubleVar()
selected_thermostream = tk.StringVar()

rm = pyvisa.ResourceManager()
listOfIntruments = list(rm.list_resources())

tk.Label(master, text="Sample ID").grid(row=0)
tk.Label(master, text="Description").grid(row=1)
tk.Label(master, text="Target").grid(row=2)

master.geometry('300x110')

e1 = tk.Entry(master, textvariable=serial_num)
e2 = tk.Entry(master, textvariable=chip_descr)
e3 = tk.Entry(master,textvariable=target_curr)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=3,column=1)

def openmaingui():
    ts_visa=selected_thermostream.get()
    sn_input=serial_num.get()
    cd_input=chip_descr.get()
    tg=target_curr.get()
    master.destroy()
    maingui(ts_visa,sn_input,cd_input,tg)

tk.Button(master, text='Quit', command=master.quit).grid(row=6, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=6, column=1, sticky=tk.W, pady=4)
tk.Button(master, text="Done", command=openmaingui).grid(row=6,column=3, sticky=tk.W, pady=4)

label = tk.Label(text="Select Thermostream").grid(row=3)
thermostream_options = ttk.Combobox(master, textvariable=selected_thermostream)
thermostream_options['values'] = listOfIntruments
thermostream_options['state'] = 'readonly'
thermostream_options.grid(row=5, column=1)

def on_ts_change(event):
    thermostream_options.bind('<<ComboboxSelected>>', on_ts_change)
    print(selected_thermostream.get())



thermostream_options.bind('<<ComboboxSelected>>', on_ts_change)


master.mainloop()


# def init_chip_form():