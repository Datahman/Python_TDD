from item import Item
import datetime
class Government_Document(Item):
	def __init__(self, id,Is_Secret,page_length, itemname,timeobj):

		super().__init__(id)
		self.itemname = itemname
		self.Is_Secret =Is_Secret
		self.page_length = page_length
		self.timeobj = timeobj.now()
	def Item_Type(self):
		return self._item_type

	def Is_Secret(self):
		return self.Is_Secret 
		
	def SetTime(self,dateime):
		self.timeobj = datetime.datetime
	def GetTime(self):
		return self.timeobj
