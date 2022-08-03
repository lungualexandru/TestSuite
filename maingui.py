import tkinter as tk
from tkinter.ttk import Frame
import easy_scpi as scpi
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

def maingui(thermo_in, chip_id, chip_descr):
    meas_voltage = open_ts(thermo_in)

    window = tk.Tk()
    window.geometry('640x480')
    swindow = Frame(window)
    swindow.grid()

    tk.Button(swindow, text='Quit', command=lambda: store_meas(swindow)).grid(row=4, column=0, sticky=tk.W, pady=4)
    tk.Button(swindow, text='Start', command=swindow.quit).grid(row=4, column=1, sticky=tk.W, pady=4)
    tk.Button(swindow, text="Stop", command=swindow.quit).grid(row=4, column=3, sticky=tk.W, pady=4)

    fig = plt.Figure(dpi=100)
    ax = fig.add_subplot(121, xlabel='Time', ylabel="Volts", title="Voltage over time", )
    xs = []
    ys = []
    canvas = FigureCanvasTkAgg(fig, master=swindow)
    canvas.get_tk_widget().grid(row=5, column=0)
    canvas.draw()

    def generate_animation(i, xarr, yarr):
        vlt = float(measure_volts(meas_voltage))
        yarr.append(vlt)
        xarr.append(yarr.index(vlt))
        xarr = xarr[-20:]
        yarr = yarr[-20:]
        ax.plot(xarr, yarr, color="red")
        plt.xticks(rotation=60, ha='right')
        plt.subplots_adjust(bottom=0.30)

    an = animation.FuncAnimation(fig, generate_animation, fargs=(xs, ys), interval=1000)

    swindow.mainloop()


def store_meas(dt):
    print("thois should store", dt)


def measure_volts(inst):
    return inst.measure.current()


def open_ts(thermo_resource):
    dmm = scpi.Instrument(thermo_resource)
    dmm.connect()
    return dmm
