import datetime
""" Person class with name attribute.
    Real life anaglous: Library customers """
class Person():
	'''Initialize person '''
	def __init__(self,name,timeobj):#,userlist):
		self.name = name
		self.timeobj = timeobj

	def PrintName(self):
		return ("Customer name : %s "% self._name) 

	def SetTime(self,dateime):
		self.timeobj = datetime.datetime
        
	def GetTime(self):
		return self.timeobj