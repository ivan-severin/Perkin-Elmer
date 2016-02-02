#!/usr/bin/python2

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial


device_port = serial.Serial("/dev/ttyUSB0" , 9600, timeout=5)
fo = open("foo.txt", "w")

def data_gen(t=0):
    #t = 4000
    while True:
        #if t > 200: 
	t +=1 
	s1 = device_port.readline()
        y1 = float(s1.split()[0])
        y2 = float(s1.split()[1])
	yield y1, y2

def init():

    ax.set_ylim(4000, 200)
    ax.set_xlim(0, 100)
    ax.invert_xaxis()  
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], 'go')
ax.grid()
xdata, ydata = [], []

print "T, 50ms \t briteness \n"


def run(data):
    # update the data
    t, y = data
    print t, y
    xdata.append(t)
    ydata.append(y)
    #fo.write(t, y)
    xmin, xmax = ax.get_xlim()
    #print xmin, xmax
    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                              repeat=False, init_func=init)
plt.show()

fo.close()
device_port.close()
