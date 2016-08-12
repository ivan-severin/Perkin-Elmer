import sys
import glob
import serial
import numpy as np

from  PyQt4 import QtCore


def serial_ports():
    """
    Finds all serial ports (cross platform)
    :return: array of ports
    """
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


class Data(QtCore.QThread):
    """
    It provides collecting and performing all data, which comes from Serial port


    """

    def __init__(self, port_adr = '/dev/ttyUSB0', port_baud=34800):
        QtCore.QThread.__init__(self)
        # super( Data, self).__init__()
        self.port = port_adr
        self.baud = port_baud

        self.device = serial.Serial(self.port, self.baud)


        #  print 'Cant find Arduio'
        self.data_store = None

        self.x_data = []
        self.y_data = []
        self.t_data = []
        # data = x_data, y_data

    def run(self):
        for i in range(10):
            self.sleep(1)
            self.emit(QtCore.SIGNAL('run_signal(float, float)'), i, i**3)

    def get_data(self, n=100):
        """
        type: () -> float, float, float
        # Function reads n lines from serial port,
        # append to array (x_data[], y_data[]) return array
        # of pairs which was rad

        """

        try:

            # self.device.write('r')
            # for i in range(n):

            line = self.device.readline()
            data = [float(val) for val in line.split()]

            if len(data) == 2:
                self.x_data.append(data[0])
                self.y_data.append(data[1])
        except (OSError, serial.SerialException, AttributeError):
            print('No Arduio')
        return self.x_data, self.y_data

    def send_setting(self):

        pass
