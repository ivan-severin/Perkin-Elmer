#!/usr/bin/python

import serial


device_port = serial.Serial("/dev/ttyUSB0" , 115200, timeout=30)
while 1:
    answer = device_port.read(6)
    print answer
device_port.close()
