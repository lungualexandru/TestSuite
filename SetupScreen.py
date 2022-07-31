import pyvisa
from tkinter import *
import numpy as np

rm = pyvisa.ResourceManager()
listOfIntruments =np.asarray(rm.list_resources())
listOfIntruments.flatten()
master = Tk()
variable = StringVar(master)
variable.set(listOfIntruments[0])
w=OptionMenu(master,variable,*listOfIntruments)
w.pack()
mainloop()