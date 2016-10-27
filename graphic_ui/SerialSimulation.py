#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Simple Simulation Module for emulate Arduino output from spectrometr.

 It reads file with IR spectrum and returns number by number.
"""
import time


class SerialException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise SerialException(2 * 2)
except SerialException as e:
    print 'My exception occurred, value:', e.value


class Serial(SerialException):
    """
    Many of the arguments have default values and can be
    skipped when calling the constructor

    """

    def __init__(self, port='COM1', baudrate=19200, timeout=1,
                 bytesize=8, parity='N', stopbits=1, xonxoff=0,
                 rtscts=0):
        self.name = port
        self.port = port
        self.timeout = timeout
        self.parity = parity
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.stopbits = stopbits
        self.xonxoff = xonxoff
        self.rtscts = rtscts
        self._isOpen = True
        self._receivedData = ""
        self.__finame = "../spectres/spectr.csv"
        self.__data = open(self.__finame, 'r')

    @property
    def isOpen(self):
        """Returns True if the port to the Arduino is open.  False otherwise"""
        return self._isOpen

    def open(self):
        """ Opens the port"""
        self._isOpen = True

    def close(self):
        """ Closes the port"""
        self._isOpen = False

    def write(self, string):
        """ Writes a string of characters to the Arduino"""
        print('Arduino got: "' + string + '"')
        self._receivedData += string

    def read(self, n=1):
        """
        Reads n characters from the fake Arduino. Actually n characters
        are read from the string _data and returned to the caller.
        """
        s = self.__data[0:n]
        self.__data = self.__data[n:]
        # print( "read: now self._data = ", self._data )
        return s

    def readline(self):
        """ Reads characters from the fake Arduino until a \n is found"""
        time.sleep(0.2)
        return self.__data.readline()

    def __str__(self):
        """ Returns a string representation of the serial class"""
        return "Serial<id=0xa81c10, open=%s>( port='%s', baudrate=%d," \
               % (str(self.isOpen), self.port, self.baudrate) \
               + " bytesize=%d, parity='%s', stopbits=%d, xonxoff=%d, rtscts=%d)" \
                 % (self.bytesize, self.parity, self.stopbits, self.xonxoff,
                    self.rtscts)


def main():
    s = Serial()
    for i in range(100):
        print s.readline()


if __name__ == '__main__':
    main()
