class  Data(object):
	"""docstring for  Data"""
	def __init__(self):
		super( Data, self).__init__()
		import serial
		self.device_port = serial.Serial("/dev/ttyUSB0" , 9600, timeout=100)
		self.x_data = []
		self.y_data = []
		#data = x_data, y_data


	def getData(self):
		s1 = self.device_port.readline()
		self.x_data.append(float(s1.split()[0]))
		self.y_data.append(float(s1.split()[1]))
		print self.x_data,self.y_data 
		print 
		return self.x_data, self.y_data
data = Data()
while true:
	data.getData()