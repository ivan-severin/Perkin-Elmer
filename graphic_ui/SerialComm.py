#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtCore
# import numpy as np
import sys
import glob
# import serial
import SerialSimulation as serial


class SerialComm(QtCore.QThread):
    def __init__(self, port='/dev/ttyUSB0', baud=38400,  timeout=0.1):
        """
        This class provide simple interface of communication with Serial port for other classes
        :param port: The COM port to open. Must be recognized by the system.
        :param baud: Bit rate of Asynchronous Serial port
        :param timeout: Period of waiting for calling to port
        """
        QtCore.QThread.__init__(self)

        self.port = port
        self.baud = baud
        self.__conn_state = False
        self.timeout = timeout
        self.ser = None

    def run(self):
        """
        Starts Thread which reads data from serial port in and emit :signal:
        of buff array with b_size
        """
        while self.__conn_state:
            try:
                x, y = self.load_data()
                self.emit(QtCore.SIGNAL('run_signal(float,float)'), x, y)
            except ValueError:
                print ValueError

    def connect(self, **kwargs):
        # type: () -> object
        """

        :return:
        """
        try:
            # serial.Serial.__init__(self, port=self.port, baudrate=self.baud, timeout=self.timeout)
            if self.ser:
                self.ser.close()

            self.ser = serial.Serial(port=self.port, baudrate=self.baud)
            # self.ser.open()
            self.__conn_state = True
            print("Successfully connected to port %r." % self.port)
            return [1, 'connected']
        except(OSError, serial.SerialException, AttributeError):
            self.__conn_state = False
            print ('no hardware found')
            return [0, 'no hardware found']

    def disconnect(self, **kwargs):
        """
        Close serial connection
        """

        self.__conn_state = False
        self.ser.close()
        print("Successfully disconnected to port %r." % self.port)

    @property
    def is_connected(self):
        """
        :return: State of connection (True/False)
        """
        # Is the computer connected with the Serial Port?
        try:
            return self.__conn_state
        except(OSError, serial.SerialException):
            return False

    def load_data(self):
        """
        type: () -> float, float, float
        or
        type: () -> float, float
        # Function reads n lines from serial port,
        # append to array (x_data[], y_data[]) return array
        # of pairs which was rad
        """
        data = []
        try:
            line = self.ser.readline()
            data = [float(val) for val in line.split()]

        except (ValueError, TypeError, OSError, serial.SerialException):
            print('No Arduino')
            print(line)
            print(ValueError)

        return data

    def send_data(self, command):
        """
        Sends data to serial port
        :param command: byte array of commands
        """
        try:
            self.ser.write(command)
        except (OSError, serial.SerialException) as e:
            print('Error sending message "%s" to Arduino:\n%s' % (command, e))

    @staticmethod
    def find_ports():
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
