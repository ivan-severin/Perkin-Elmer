#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This  is simple program collecting and performing
__data from spectrometer Perkin Elmer 599b.

Used modules: PyQt4,  pyqtgraph, os, sys, __data (Serial)
"""

from PyQt4 import QtGui
import pyqtgraph as pg
from Data import *
from SerialComm import *


class ApplicationWindow(QtGui.QMainWindow):
    """
    This  is simple program collecting and performing
    __data from spectrometer Perkin Elmer 599b.
    """

    def __init__(self):
        """

        """
        QtGui.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Perkin Elmer Spectro")
        self.setWindowIcon(QtGui.QIcon('resources/icon/icon2.png'))

        # Create file menu
        self.__file_menu = QtGui.QMenu('&File', self)
        self.__file_menu.addAction('&Quit', self.file_quit, QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.__file_menu)

        # Create help menu
        self.__help_menu = QtGui.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.__help_menu)
        # self.__help_menu.addAction('&About', self.about)

        # Define main layout
        self.main_widget = QtGui.QWidget(self)
        __layout = QtGui.QGridLayout(self.main_widget)

        # Add buttons
        self.__btn_start_stop = QtGui.QPushButton('Start')
        self.__btn_clear = QtGui.QPushButton('Clear')
        # self.__btn_clear.setDisabled(True)

        # Create & Define plot from PyQtgraph
        self.__main_plot = pg.PlotWidget(title="Main plow Window")
        self.__rs_plot = pg.PlotWidget(title="Region Selection Window")
        self.__main_plot.plotItem.addItem(self.__rs_plot.plotItem)
        self.__curve = self.__main_plot.plot()
        self.__curve1 = self.__main_plot.plot()

        # Add long plot of region selection
        self.lr = pg.LinearRegionItem([0, 200])
        self.lr.setZValue(-10)
        # self.__rs_plot.addItem(self.lr)
        self.set_plot_conf(self.__main_plot)
        self.set_plot_conf(self.__rs_plot)

        self.lr.sigRegionChanged.connect(lambda:
                                         self.__main_plot.setXRange(padding=0,
                                                                    *self.lr.getRegion()))
        self.__rs_plot.sigXRangeChanged.connect(
            lambda: self.lr.setRegion(self.__main_plot.plotItem.getViewBox().viewRange()[0]))
        # Create instance of some data, which we should plot
        self.__dev = SerialComm()
        self.__data = Data()

        # Add some objects on Grid Layout (x position, y position, eat x rows, eat y columns )
        __layout.addWidget(self.__btn_start_stop, 9, 0, 1, 2)
        __layout.addWidget(self.__btn_clear, 10, 0, 1, 2)
        __layout.addWidget(self.__main_plot, 1, 4, 11, 1)  # __plot goes on right side, spanning 11 rows
        # __layout.addWidget(self.__rs_plot, 12, 4)  # __plot goes on right side, spanning 11 rows

        # Define signal&slots for buttons and Data instance
        self.connect(self.__btn_start_stop, QtCore.SIGNAL('clicked()'), self.on_clicked)
        self.connect(self.__btn_clear, QtCore.SIGNAL('clicked()'), self.clear_screen)

        self.connect(self.__dev,
                     QtCore.SIGNAL('run_signal(float, float)'),
                     self.on_change, QtCore.Qt.QueuedConnection)
        self.connect(self.__dev, QtCore.SIGNAL('started()'), self.on_started)
        self.connect(self.__dev, QtCore.SIGNAL('finished()'), self.on_finished)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

    def on_change(self, a, b):
        self.__data.x_data.append(a)
        self.__data.y_data.append(b)
        self.__curve.setData(self.__data.x_data, self.__data.y_data, _callSync='off')

    def on_clicked(self):
        # self.__btn_start.setDisabled(True)
        if not self.__dev.is_connected:
            self.__btn_start_stop.setText("Stop")
            self.__dev.connect()
            self.__dev.start()
        else:
            self.__btn_start_stop.setText("Start")
            self.__dev.disconnect()

    def on_started(self):
        self.statusBar().showMessage("Connected and Started!", 2000)

    def on_finished(self):
        self.statusBar().showMessage("Finished!", 2000)

    def clear_screen(self):
        self.__data.x_data = []
        self.__data.y_data = []
        # self.__curve.setData([], [])
        # self.__btn_clear.setDisabled(True)

    @staticmethod
    def set_plot_conf(obj):
        """
        Sets some pyQtGraph settings such as WindowTitle,
        OX and OY labels, measuring units.
        :type obj: pyqtpraph Widqget
        """
        # self.__plot.setWindowTitle('pyqtgraph example: __plotSpeedTest')
        try:
            obj.setLabel('bottom', 'WaveNumber', units='1/cm')
            obj.setLabel('left', 'Transmittance')
            obj.showGrid(x=True, y=True)
            obj.invertX()
        except AttributeError:
            print(AttributeError)
            pass

    def update_plot(self):
        """
        Set new __data for pyQtGraph: __curve and __curve1 (in case three rows of __data),
        for every frame of new frame.
        :return: self
        """
        # print type(self.__data.get_data())
        try:
            t, x, y = self.__dev.get_data()
            self.__curve.setData(x=t, y=x, pen='r', symbol='o', symbolPen='r')
            # assert isinstance(self.__curve1.setData, object)
            self.__curve1.setData(x=t, y=y, pen='g', symbol='s', symbolPen='g')
        except ValueError:
            x, y = self.__dev.get_data()
            self.__curve.setData(x=x, y=y, pen='g')

    def file_quit(self):

        if self.__dev.isRunning():
            self.__dev.disconnect()

    def closeEvent(self, event):
        self.file_quit()
        self.hide()
        event.accept()
        # def about(self):
        #     QtGui.QMessageBox.about(self,
        #                             'About',
        #                             'Copyright of Ivan Severin. \n'
        #                             'It may be used and modified with no restriction; '
        #                             'raw copies as well as modified versions may be '
        #                             'distributed without limitation.')


def main():
    q_app = QtGui.QApplication(sys.argv)
    aw = ApplicationWindow()
    aw.show()
    sys.exit(q_app.exec_())


if __name__ == '__main__':
    main()
