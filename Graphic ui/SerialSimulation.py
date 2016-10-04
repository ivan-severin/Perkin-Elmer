#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Simple Simulation Module for emulate Arduino output from spectrometr.

 It reads file with IR spectrum and returns number by number.
"""
import serial



class SerialSimulation:
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
        # self._data = "It was the best of times.\nIt was the worst of times.\n"
        self._data = open('../../Test_analog_transf/test_spectr11.csv', 'r')


    ## isOpen()
    # returns True if the port to the Arduino is open.  False otherwise
    def isOpen(self):
        return self._isOpen

    ## open()
    # opens the port
    def open(self):
        self._isOpen = True

    ## close()
    # closes the port
    def close(self):
        self._isOpen = False

    ## write()
    # writes a string of characters to the Arduino
    def write(self, string):
        print('Arduino got: "' + string + '"')
        self._receivedData += string

    ## read()
    # reads n characters from the fake Arduino. Actually n characters
    # are read from the string _data and returned to the caller.
    def read(self, n=1):
        s = self._data[0:n]
        self._data = self._data[n:]
        # print( "read: now self._data = ", self._data )
        return s

    ## readline()
    # reads characters from the fake Arduino until a \n is found.
    def readline(self):

        s = self._data.readline()

        if len(s) < 0:
            raise serial.SerialException

    ## __str__()
    # returns a string representation of the serial class
    def __str__(self):
        return "Serial<id=0xa81c10, open=%s>( port='%s', baudrate=%d," \
               % (str(self.isOpen), self.port, self.baudrate) \
               + " bytesize=%d, parity='%s', stopbits=%d, xonxoff=%d, rtscts=%d)" \
                 % (self.bytesize, self.parity, self.stopbits, self.xonxoff,
                    self.rtscts)


class SerialException(Exception):
   def __init__(self, value):
       self.value = value

   def __str__(self):
      return repr(self.value)

try:
     raise SerialException(2*2)
except SerialException as e:
     print 'My exception occurred, value:', e.value




def main():
    s = SerialSimulation()
    for i in range(100):
        print s.readline()


if __name__ == '__main__':
    main()
