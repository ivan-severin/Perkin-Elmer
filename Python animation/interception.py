#!/usr/bin/python2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial


device_port = serial.Serial("/dev/ttyUSB0" , 9600, timeout=1000)
while 1:
    s1 = device_port.readline()
    
    y1 = int(s1.split()[0])
    y2 = int(s1.split()[1])
    print y1, y2
device_port.close()


