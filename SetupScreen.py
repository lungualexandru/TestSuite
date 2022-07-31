import pyvisa
from tkinter import *
import numpy as np

rm = pyvisa.ResourceManager()
listOfIntruments =np.asarray(rm.list_resources())
print("The following instruments are available", listOfIntruments)

master = Tk()
variable = StringVar(master)
variable.set(Options[0])
w = [OptionMenu(master, instr, *Options) for instr in listOfIntruments]
[f.pack() for f in w]

mainloop()