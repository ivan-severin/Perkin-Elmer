#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This  is simple program collecting and performing
__data from spectrometer Perkin Elmer 599b.

Used modules: PyQt4,  pyqtgraph, os, sys, __data (Serial)
"""

from PyQt4 import QtGui, QtCore
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
        self.__btn_add = QtGui.QPushButton('Add plot')
        self.__btn_clear.setDisabled(True)

        # Add Combo box
        self.__cb = QtGui.QComboBox()
        # Create & Define plot from PyQtgraph
        self.__main_plot = pg.PlotWidget()
        self.__rs_plot = pg.PlotWidget()

        self.curve = self.__main_plot.plot()
        self.curve1 = self.__rs_plot.plot()

        # Set X Range
        self.__rs_plot.setXRange(0.0, 4000)
        self.__main_plot.setXRange(0.0, 200)
        self.__main_plot.setYRange(0.0, 1024)

        # Add long plot of region selection
        self.lr = pg.LinearRegionItem([0, 200])
        self.lr.setZValue(10)
        self.__rs_plot.addItem(self.lr)

        # Set config for each Plot Widget
        self.set_plot_conf(self.__main_plot)
        self.set_plot_conf(self.__rs_plot)

        # Defining cross hair
        self.v_line = pg.InfiniteLine(angle=90, pos=-1000, movable=False)
        self.h_line = pg.InfiniteLine(angle=0, pos=-1000, movable=False)

        # Defining the label for numeric value of every dot in spectrum
        self.xy_label = pg.LabelItem(justify='right', text='')

        # Adding Two lines and label to plot
        self.__main_plot.addItem(self.v_line)
        self.__main_plot.addItem(self.h_line)
        self.__main_plot.addItem(self.xy_label)

        # Create instance of some data, which we should plot
        self.__dev = SerialComm()
        self.__data = [Data()]

        self.index = self.__cb.currentIndex()
        self.__cb.addItem('Default plot')
        self.__cb.setEditable(True)

        self.timer = QtCore.QTimer()

        # Add some objects on Grid Layout (x position, y position, eat x rows, eat y columns )
        __layout.addWidget(self.__btn_start_stop, 2, 0, 1, 2)
        __layout.addWidget(self.__btn_clear, 3, 0)
        __layout.addWidget(self.__btn_add, 3, 1)
        __layout.addWidget(self.__cb, 1, 0, 1, 2)
        __layout.addWidget(self.__rs_plot, 1, 4, 10, 1)  # __plot goes on right side, spanning 11 rows
        __layout.addWidget(self.__main_plot, 11, 4, 2, 1)  # __plot goes on right side, spanning 11 rows

        # Define signal&slots for buttons and Data instance
        self.connect(self.__btn_start_stop, QtCore.SIGNAL('clicked()'), self.clicked_start_stop)
        self.connect(self.__btn_clear, QtCore.SIGNAL('clicked()'), self.clicked_clear_data)
        self.connect(self.__btn_add, QtCore.SIGNAL('clicked()'), self.clicked_add_data)
        self.connect(self.__cb, QtCore.SIGNAL('currentIndexChanged()'), self.change_current_plot)
        # self.__cb.currentIndexChanged(self.change_current_plot)

        self.connect(self.__dev, QtCore.SIGNAL('started()'), self.on_started)
        self.connect(self.__dev, QtCore.SIGNAL('finished()'), self.on_finished)

        # Signal& slot connection for Thread which reads data from Serial port
        self.connect(self.__dev,
                     QtCore.SIGNAL('run_signal(float,float)'),
                     self.on_change, QtCore.Qt.QueuedConnection)

        # Signal& slot connection
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.re_plot)

        # Making signals for resizing __main_plot when region changed
        self.lr.sigRegionChanged.connect(
            lambda: self.__main_plot.setXRange(padding=0, *self.lr.getRegion()))

        self.__rs_plot.sigXRangeChanged.connect(
            lambda: self.lr.setRegion(self.__main_plot.plotItem.getViewBox().viewRange()[0]))

        self.__main_plot.plotItem.sigXRangeChanged.connect(
            lambda: self.lr.setRegion(self.__main_plot.plotItem.getViewBox().viewRange()[0])
        )

        self.__main_plot.scene().sigMouseMoved.connect(self.mouse_moved)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

    def mouse_moved(self, evt):
        """
        Actions for performing changing cross hair lines from mouse moving
        :param evt: type: QPointF. Coordinates of Mouse on Plot.
        """

        # performing Moving Slot
        if self.__main_plot.plotItem.sceneBoundingRect().contains(evt):
            mouse_point = self.__main_plot.plotItem.vb.mapSceneToView(evt)
            index = int(mouse_point.x())
            if 0 < index < len(self.__data[self.index].x_data):
                self.xy_label.setText(
                    "<span style='font-size: 12pt'>x=%0.1f</span>,   "
                    "<span style='color: red'>y1=%0.1f</span>"
                    % (mouse_point.x(), self.__data[self.index].y_data[index]))
                self.v_line.setPos(mouse_point.x())
                self.h_line.setPos(self.__data[self.index].y_data[index])

    def on_change(self, a, b):
        index = self.__cb.currentIndex()
        self.__data[index].x_data.append(a)
        self.__data[index].y_data.append(b)
        # self.__curve.setData(self.__data.x_data, self.__data.y_data, _callSync='off')

    def clicked_start_stop(self):
        """
        Slot Function for Start/Stop button
        :return:
        """
        index = self.__cb.currentIndex()
        if len(self.__data[index].x_data) > 1:
            self.__btn_clear.setDisabled(False)

        if not self.__dev.is_connected:
            self.__btn_start_stop.setText("Stop")
            self.__dev.connect()
            self.__dev.start()
        else:
            self.__btn_start_stop.setText("Start")
            self.__dev.disconnect()
            self.timer.stop()

    def on_started(self):
        """
        Slot Function for starting Thread.
        :return:
        """
        self.statusBar().showMessage("Connected and Started!", 2000)

        self.timer.start(100)
        print ("Timer started")

    def on_finished(self):
        self.statusBar().showMessage("Finished!", 2000)
        self.timer.stop()

    def clicked_clear_data(self):
        self.__data.pop()

    def clicked_add_data(self):
        name, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()", "Plot name:", QtGui.QLineEdit.Normal)

        if ok:
            # name.setComboBoxEditable()
            self.__data.append(Data())
        # print name.getItem()
            self.__cb.addItem(name)

    def change_current_plot(self):
        x = self.__data[self.index].x_data
        y = self.__data[self.index].y_data
        self.curve1.setData(x, y, pen=(0, 0, 255))

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

    def re_plot(self):
        """

        :return:
        """
        try:
            self.curve.setData(self.__data[self.index].x_data, self.__data[self.index].y_data)
            self.curve1.setData(self.__data[self.index].x_data, self.__data[self.index].y_data)
        except Exception as e:
            print(e)
            return 1, e
        return 0

    def file_quit(self):
        """

        :return:
        """

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
