#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from mpl import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MplMainWindow(object):
    def setupUi(self, MplMainWindow):
        MplMainWindow.setObjectName(_fromUtf8("MplMainWindow"))
        MplMainWindow.resize(724, 484)

        self.centralwidget = QtGui.QWidget(MplMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(450, 40, 91, 149))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))


        self.ScanTimeLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.ScanTimeLayout.setObjectName(_fromUtf8("ScanTimeLayout"))

        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cantarell"))
        font.setPointSize(12)
        font.setItalic(False)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.ScanTimeLayout.addWidget(self.label)
        self.rbWide6 = QtGui.QRadioButton(self.layoutWidget)
        self.rbWide6.setObjectName(_fromUtf8("rbWide6"))


        self.ScanTimeLayout.addWidget(self.rbWide6)
        self.rbWide3 = QtGui.QRadioButton(self.layoutWidget)
        self.rbWide3.setObjectName(_fromUtf8("rbWide3"))


        self.ScanTimeLayout.addWidget(self.rbWide3)
        self.rbNorm12 = QtGui.QRadioButton(self.layoutWidget)
        self.rbNorm12.setChecked(True)
        self.rbNorm12.setObjectName(_fromUtf8("rbNorm12"))


        self.ScanTimeLayout.addWidget(self.rbNorm12)
        self.rbNarr60 = QtGui.QRadioButton(self.layoutWidget)
        self.rbNarr60.setObjectName(_fromUtf8("rbNarr60"))


        self.ScanTimeLayout.addWidget(self.rbNarr60)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(450, 190, 125, 121))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))

        self.MultiplerLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.MultiplerLayout.setObjectName(_fromUtf8("MultiplerLayout"))

        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)

        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.MultiplerLayout.addWidget(self.label_2)
        self.radioButton = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))

        self.MultiplerLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))

        self.MultiplerLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.layoutWidget1)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))

        self.MultiplerLayout.addWidget(self.radioButton_3)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(560, 40, 124, 151))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))

        self.ChartExpansionLoyaut = QtGui.QVBoxLayout(self.layoutWidget2)
        self.ChartExpansionLoyaut.setObjectName(_fromUtf8("ChartExpansionLoyaut"))

        self.label_3 = QtGui.QLabel(self.layoutWidget2)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.ChartExpansionLoyaut.addWidget(self.label_3)
        self.radioButton_5 = QtGui.QRadioButton(self.layoutWidget2)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))

        self.ChartExpansionLoyaut.addWidget(self.radioButton_5)
        self.radioButton_6 = QtGui.QRadioButton(self.layoutWidget2)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))

        self.ChartExpansionLoyaut.addWidget(self.radioButton_6)
        self.radioButton_4 = QtGui.QRadioButton(self.layoutWidget2)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))

        self.ChartExpansionLoyaut.addWidget(self.radioButton_4)
        self.radioButton_7 = QtGui.QRadioButton(self.layoutWidget2)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))

        self.ChartExpansionLoyaut.addWidget(self.radioButton_7)
        self.layoutWidget3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(580, 200, 113, 92))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))

        self.CheckStatusLayout = QtGui.QVBoxLayout(self.layoutWidget3)
        self.CheckStatusLayout.setObjectName(_fromUtf8("CheckStatusLayout"))
        self.TimeDrive = QtGui.QCheckBox(self.layoutWidget3)
        self.TimeDrive.setObjectName(_fromUtf8("TimeDrive"))


        self.CheckStatusLayout.addWidget(self.TimeDrive)
        self.Index = QtGui.QCheckBox(self.layoutWidget3)
        self.Index.setObjectName(_fromUtf8("Index"))

        self.CheckStatusLayout.addWidget(self.Index)
        self.checkBox = QtGui.QCheckBox(self.layoutWidget3)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.CheckStatusLayout.addWidget(self.checkBox)
        self.layoutWidget4 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(440, 330, 271, 33))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))

        self.StatusLoyaut = QtGui.QHBoxLayout(self.layoutWidget4)
        self.StatusLoyaut.setObjectName(_fromUtf8("StatusLoyaut"))

        self.pushButton = QtGui.QPushButton(self.layoutWidget4)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))


        self.StatusLoyaut.addWidget(self.pushButton)
        self.label_5 = QtGui.QLabel(self.layoutWidget4)
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.StatusLoyaut.addWidget(self.label_5)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 421, 391))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.mpl = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.mpl.setObjectName(_fromUtf8("mpl"))


        MplMainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtGui.QMenuBar(MplMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 724, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MplMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MplMainWindow)
        self.statusbar.setAccessibleName(_fromUtf8(""))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MplMainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MplMainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MplMainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionClose = QtGui.QAction(MplMainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MplMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MplMainWindow)

    def retranslateUi(self, MplMainWindow):
        MplMainWindow.setWindowTitle(_translate("MplMainWindow", "MainWindow", None))
        self.label.setText(_translate("MplMainWindow", "Scan Time ", None))
        self.rbWide6.setText(_translate("MplMainWindow", "Wide", None))
        self.rbWide3.setText(_translate("MplMainWindow", "Widest", None))
        self.rbNorm12.setText(_translate("MplMainWindow", "Norm", None))
        self.rbNarr60.setText(_translate("MplMainWindow", "Narrow", None))
        self.label_2.setText(_translate("MplMainWindow", "Multiler (Noise)", None))
        self.radioButton.setText(_translate("MplMainWindow", "1 (1)", None))
        self.radioButton_2.setText(_translate("MplMainWindow", "4 (1/2)", None))
        self.radioButton_3.setText(_translate("MplMainWindow", "16 (1/4)", None))
        self.label_3.setText(_translate("MplMainWindow", "Chart expansion", None))
        self.radioButton_5.setText(_translate("MplMainWindow", "1.0", None))
        self.radioButton_6.setText(_translate("MplMainWindow", "5.0", None))
        self.radioButton_4.setText(_translate("MplMainWindow", "0.5", None))
        self.radioButton_7.setText(_translate("MplMainWindow", "20.0", None))
        self.TimeDrive.setText(_translate("MplMainWindow", "Time Drive", None))
        self.Index.setText(_translate("MplMainWindow", "Index", None))
        self.checkBox.setText(_translate("MplMainWindow", "Abs", None))
        self.pushButton.setText(_translate("MplMainWindow", "Check Staus", None))
        self.label_5.setText(_translate("MplMainWindow", "unconnected", None))
        self.menuFile.setTitle(_translate("MplMainWindow", "File", None))
        self.actionOpen.setText(_translate("MplMainWindow", "Open", None))
        self.actionSave.setText(_translate("MplMainWindow", "Save", None))
        self.actionClose.setText(_translate("MplMainWindow", "Close", None))


