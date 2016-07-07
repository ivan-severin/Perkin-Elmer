#!/usr/bin/env python
import pyqtgraph as pg
from Data import *
class PgCanvas(object):
 	"""docstring for PgCanvas"""
 	def __init__(self, arg):
 		super(PgCanvas, self).__init__()
 		self.arg = arg
 		self.p = pg.plot()
 		self.p.setWindowTitle('Stirling engine ')
 		self.curve = self.p.plot()
 		self.data = Data()

 		timer = QtCore.QTimer(self)
		timer.timeout.connect(self.update_figure)
		timer.start(0)

 	def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        #l = [random.randint(0, 10) for i in range(4)]
        x, y = self.data.getData()
        
        

        
