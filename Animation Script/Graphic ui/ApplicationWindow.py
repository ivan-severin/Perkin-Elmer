#!/usr/bin/env python
# @name = ...
import sys
import os
import numpy as np
from PyQt4 import QtGui, QtCore
import pyqtgraph as pg

progname = os.path.basename(sys.argv[0])

progversion = "0.1"

# from MyMplCanvas import *

from Data import *


class ApplicationWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # self.setGeometry(50, 50, 500, 300)


        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QtGui.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit, QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtGui.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QtGui.QWidget(self)

        layout = QtGui.QGridLayout(self.main_widget)

        self.scan_time_group = QtGui.QButtonGroup()
        self.chart_expansion_group = QtGui.QButtonGroup()
        self.multipler_noize_group = QtGui.QButtonGroup()

        self.scan_time = [QtGui.QLabel('Scan Time'), QtGui.QRadioButton('Wide'), QtGui.QRadioButton('Widest'),
                          QtGui.QRadioButton('Norm'), QtGui.QRadioButton('Narrow')]
        self.chart_expansion = [QtGui.QLabel('Chart Expansion'), QtGui.QRadioButton('0.5'), QtGui.QRadioButton('1.0'),
                                QtGui.QRadioButton('5.0'), QtGui.QRadioButton('20.0')]
        self.multipler_noize = [QtGui.QLabel('Multipler noise'), QtGui.QRadioButton('1 (1)'),
                                QtGui.QRadioButton('4 (1/2)'), QtGui.QRadioButton('16 (1/4)')]
        self.checkbox = [QtGui.QCheckBox('Time Drive'), QtGui.QCheckBox('Index'), QtGui.QCheckBox('ABS')]

        self.btn = QtGui.QPushButton('Send Settings')

        self.scan_time[3].setChecked(True)
        self.chart_expansion[2].setChecked(True)
        self.multipler_noize[1].setChecked(True)

        layout.addWidget(self.scan_time[0], 0, 0)
        layout.addWidget(self.chart_expansion[0], 0, 1)
        layout.addWidget(self.multipler_noize[0], len(self.chart_expansion), 0)

        for i in range(1, len(self.scan_time)):
            layout.addWidget(self.scan_time[i], i, 0)
            self.scan_time_group.addButton(self.scan_time[i], i)
            # self.scan_time[i].clicked().connect(self.scan_time_clicked)
        for i in range(1, len(self.chart_expansion)):
            layout.addWidget(self.chart_expansion[i], i, 1)
            self.chart_expansion_group.addButton(self.chart_expansion[i], i)
        for i in range(1, len(self.multipler_noize)):
            layout.addWidget(self.multipler_noize[i], len(self.scan_time) + i, 0)
            self.multipler_noize_group.addButton(self.multipler_noize[i], i)
        for i in range(len(self.checkbox)):
            layout.addWidget(self.checkbox[i], len(self.chart_expansion) + i + 1, 1)

        self.data = Data()
        self.plot = pg.PlotWidget()
        self.curve = self.plot.plot()
        self.curve1 = self.plot.plot()
        self.setconf()

        layout.addWidget(self.btn, 10, 0, 1, 2)
        self.btn.clicked.connect(self.sendSettings)

        layout.addWidget(self.plot, 0, 4, 11, 1)  # plot goes on right side, spanning 3 rows

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updateplot)
        timer.start(5)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail !", 2000)

    def sendSettings(self):
        s = '9'
        for item in self.scan_time, self.chart_expansion, self.multipler_noize:
            s += self.get_checked_items(item)
        for item in self.checkbox:
            if item.checkState():
                s += '1'
            else:
                s += '0'
        print(s)
        print (len(s))

    def setconf(self):
        # type: () -> None
        self.plot.setWindowTitle('pyqtgraph example: PlotSpeedTest')
        self.plot.setLabel('bottom', 'WaveNumber', units='1/cm')
        self.plot.setLabel('left', 'Intencivity')
        self.plot.showGrid(x=True, y=True)

    def updateplot(self):
        # print type(self.data.getData())
        try:
            t, x, y = self.data.getData()
            self.curve.setData(x=t, y=x, pen='r', symbol='o', symbolPen='r')
            self.curve1.setData(x=t, y=y, pen='g', symbol='s', symbolPen='g')
        except ValueError:
            x, y = self.data.getData()
            self.curve.setData(x=x, y=y, pen='g')

    @staticmethod
    def getCheckedItems(radio_buttons=None):
        if radio_buttons is None:
            radio_buttons = [QtGui.QRadioButton]
        s = ''
        for i in range(1, len(radio_buttons)):
            if radio_buttons[i].isChecked():
                s += str(i)
                # print (s)
        return s

    def fileQuit(self):
        self.close()

    def closeEvent(self):
        self.fileQuit()

    def about(self):
        QtGui.QMessageBox.about(self, "About", """_____.py
Copyright 2016 Florent Rougon, 2006 Darren Dale


It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation.""")


if __name__ == '__main__':
    qApp = QtGui.QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("%s" % progname)
    aw.show()
    sys.exit(qApp.exec_())
# qApp.exec_()
