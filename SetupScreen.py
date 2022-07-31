import pyvisa
from tkinter import *
import numpy as np

rm = pyvisa.ResourceManager()
listOfIntruments = np.asarray(rm.list_resources())
listOfIntruments.flatten()

master = Tk()
master.title("Select Instrument")
master.geometry('640x480')

variable = StringVar(master)
variable.set(listOfIntruments[0])

variable1 = StringVar(master)
variable1.set(listOfIntruments[0])

variable2 = StringVar(master)
variable2.set(listOfIntruments[0])

variable3 = StringVar(master)
variable3.set(listOfIntruments[0])

select_instr_scope = Label(master, text="Select Oscilloscope")
select_instr_scope.grid(row=0,column=0)

select_instr_smu = Label(master, text="Select SourceMeter")
select_instr_smu.grid(row=0, column=1)

select_instr_psu = Label(master, text="Select Power Supply")
select_instr_psu.grid(row=0, column=2)

select_instr_pace = Label(master, text="Select Pressure Controller")
select_instr_pace.grid(row=0, column=3)


instrlist_scope = OptionMenu(master, variable, *listOfIntruments)
instrlist_scope.grid(row=1,column=0)

instrlist_smu = OptionMenu(master, variable1, *listOfIntruments)
instrlist_smu.grid(row=1,column=1)

instrlist_psu = OptionMenu(master, variable2, *listOfIntruments)
instrlist_psu.grid(row=1,column=2)

instrlist_pace = OptionMenu(master, variable3, *listOfIntruments)
instrlist_pace.grid(row=1,column=3)


def ok_scope():
    print ("value is:" + variable.get())

button_select_scope = Button(master, text="OK", command=ok_scope)
button_select_scope.grid(row=2,column=0)

def ok_smu():
    print ("value is:" + variable1.get())

button_select_smu = Button(master, text="OK", command=ok_smu)
button_select_smu.grid(row=2,column=1)

def ok_psu():
    print ("value is:" + variable2.get())

button_select_psu = Button(master, text="OK", command=ok_psu)
button_select_psu.grid(row=2,column=2)

def ok_pace():
    print ("value is:" + variable3.get())

button_select_pace = Button(master, text="OK", command=ok_pace)
button_select_pace.grid(row=2,column=3)


mainloop()
