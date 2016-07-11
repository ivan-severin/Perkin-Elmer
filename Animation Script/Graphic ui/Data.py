
from __future__ import print_function
import sys
import glob
import serial
import numpy as np


def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class Data(object):
    """docstring for  Data"""

    def __init__(self):
        # super( Data, self).__init__()
        import serial
        if (serial_ports() != []):
            # rewrite later !!!!
            for port in serial_ports():
                self.device_port = serial.Serial(port, 9600)


                #  print 'Cant find Arduio'
        self.data_store = None

        self.x_data = []
        self.y_data = []
        self.t_data = []
        # data = x_data, y_data

    def getData(self):
        # type: () -> float, float, float
        # self.device_port.write('r')


        # try:

        try:
            line = self.device_port.readline()
            data = [float(val) for val in line.split()]

            if len(data) == 2:
                self.x_data.append(data[0])
                self.y_data.append(data[1])
                return (self.x_data, self.y_data)

            elif len(data) == 3:
                self.t_data.append(data[0])
                self.x_data.append(data[1])
                self.y_data.append(data[2])
                print(data)
                return (self.t_data, self.x_data, self.y_data)
            if len(self.x_data) > 1600:
                self.t_data = []
                self.y_data = []
                self.x_data = []
                # print(data)
        except:
            print('No Arduio')

        # print self.x_data,self.y_data
        # print x + '\t'+ y
        return self.x_data, self.y_data

    def send_setting(self):
        pass


