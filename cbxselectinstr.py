import pyvisa
from tkinter import *
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

rm = pyvisa.ResourceManager()
listOfIntruments = np.asarray(rm.list_resources())
listOfIntruments.flatten()

root = tk.Tk()

# config the root window
root.geometry('300x200')
root.resizable(False, False)
root.title('Select Instrument')

# label
label = ttk.Label(text="Select Oscilloscope")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_instr = tk.StringVar()
instr_options = ttk.Combobox(root, textvariable=selected_instr)

# get available instruments
instr_options['values'] = listOfIntruments

# prevent accidentaly writing a value in the combobox
instr_options['state'] = 'readonly'

# place the widget
instr_options.pack(fill=tk.X, padx=5, pady=5)


# bind the selected value changes
def instr_changed(event):
    instr_options.bind('<<ComboboxSelected>>', instr_changed)
    print(selected_instr.get())


instr_options.bind('<<ComboboxSelected>>', instr_changed)

chip_serial_num = tk.StringVar()
chip_serial_fld= ttk.Entry(root,textvariable=chip_serial_num)
chip_serial_fld.pack(side=tk.TOP)
root.mainloop()
