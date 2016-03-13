#!/usr/bin/env python



if __name__ == "__main__":
    import sys
    #import gui.py
    from gui import *
    app = QtGui.QApplication(sys.argv)
    MplMainWindow = QtGui.QMainWindow()
    ui = Ui_MplMainWindow()
    ui.setupUi(MplMainWindow)
    MplMainWindow.show()
    sys.exit(app.exec_())

