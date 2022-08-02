import tkinter
from Test1 import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

root = tkinter.Tk()
root.wm_title("Sweep over Temperature")
temp_array = [x for x in range(-40, 0, 1)]
tim_array = [x for x in range(0, 40, 1)]
fig = Figure(dpi=200)
fig.add_subplot(122).plot(temp_array, tim_array)


mydata = main()
yint = [float(x) for x in mydata[1::2]]
xint = [float(y) for y in  mydata[0::2]]
fig.add_subplot(121).plot(xint, yint)
fig.set_label("Voltage over Time")

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()  # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()

# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
