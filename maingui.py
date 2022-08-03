import math
import tkinter as tk
import datetime
from tkinter.ttk import Frame
import easy_scpi as scpi
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation


def maingui(thermo_in, chip_id, chip_descr, trgt):
    meas_voltage = open_ts(thermo_in)
    tolerance_lim = list(np.arange(trgt - 0.05 * trgt / 100, trgt + 0.05 * trgt / 100, trgt / 100))
    set_voltage(meas_voltage, trgt)
    window = tk.Tk()
    window.title("TempSweepOverTime")
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

    # TODO : fix yaxis scaling so that we get last reading +/- 30%
    def generate_animation(i, xarr, yarr):
        vlt = float(measure_volts(meas_voltage))
        is_on_target = math.isclose(vlt, trgt, rel_tol=0.05)
        lg = math.log1p(vlt)
        yarr.append(vlt)
        xarr.append(yarr.index(vlt))
        # x =

        xarr = [datetime.datetime.now() + datetime.timedelta(seconds=i) for i in range(len(xarr))]
        yarr = yarr[-20:]
        xarr = xarr[-20:]
        ax.clear()
        ax.plot(xarr, yarr, color="blue")
        ax.set_xlabel('Time')
        ax.set_ylabel('Current')
        # ax.set_xticks(rotation=60, ha='right')
        ax.xaxis.set_tick_params(rotation=30, labelsize=10)
        plt.gcf().autofmt_xdate()
        plt.rcParams['axes.formatter.useoffset'] = False
        plt.xticks(rotation=60, ha='right')
        plt.subplots_adjust(bottom=0.30, left= 0.30)
        print("targ", vlt)
        label = tk.Label(text="on target:{}".format(is_on_target)).grid(row=5)

    an = animation.FuncAnimation(fig, generate_animation, fargs=(xs, ys), interval=100)

    swindow.mainloop()


def store_meas(dt):
    print("thois should store", dt)


def set_voltage(ins, t):
    print('target',t,"is",ins)
    s = ins.source.voltage(t)
    print("SDs",s)
    return s


def measure_volts(inst):
    return inst.measure.voltage()


def open_ts(thermo_resource):
    dmm = scpi.Instrument(thermo_resource)
    dmm.connect()
    return dmm
