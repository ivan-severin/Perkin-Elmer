#!/usr/bin/env python



from __future__ import unicode_literals
import sys
import os
import numpy as np
from matplotlib.backends import qt_compat
use_pyside = qt_compat.QT_API == qt_compat.QT_API_PYSIDE
if use_pyside:
	from PySide import QtGui, QtCore
else:
	from PyQt4 import QtGui, QtCore



progname = os.path.basename(sys.argv[0])

progversion = "0.1"


#from MyMplCanvas import *
import pyqtgraph as pg
from Data import *

class ApplicationWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)

		#self.setGeometry(50, 50, 500, 300)


		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setWindowTitle("application main window")

		self.file_menu = QtGui.QMenu('&File', self)
		self.file_menu.addAction('&Quit', self.fileQuit,
								 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
		self.menuBar().addMenu(self.file_menu)

		self.help_menu = QtGui.QMenu('&Help', self)
		self.menuBar().addSeparator()
		self.menuBar().addMenu(self.help_menu)

		self.help_menu.addAction('&About', self.about)

		self.main_widget = QtGui.QWidget(self)
		self.data = Data()

		

		
		l = QtGui.QVBoxLayout(self.main_widget)
		#number_group=QtGui.QButtonGroup(self.main_widget) # Number group
		#r0=QtGui.QRadioButton("0")
		#r1=QtGui.QRadioButton("1")
		#number_group.addButton(r0)
		#number_group.addButton(r1)
		#letterGroup = QtGui.QButtonGroup(self.main_widget)
		#ra = QtGui.QRadioButton("a")
		#rb = QtGui.QRadioButton("b")
		#letterGroup.addButton(ra)
		#letterGroup.addButton(rb)


		#dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
		plot = pg.PlotWidget()
		l.addWidget(plot)
		timer = QtCore.QTimer()
		timer.timeout.connect(self.data.getData)
		timer.start(0)

		

		self.main_widget.setFocus()
		self.setCentralWidget(self.main_widget)

		self.statusBar().showMessage("All hail !", 2000)
	def update(self):
		self.data.getData()
	def fileQuit(self):
		self.close()

	def closeEvent(self, ce):
		self.fileQuit()

	def about(self):
		QtGui.QMessageBox.about(self, "About",
								"""_____.py 
Copyright 2016 Florent Rougon, 2006 Darren Dale


It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation."""
								)


qApp = QtGui.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("%s" % progname)
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()