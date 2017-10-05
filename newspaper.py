from item import Item
import datetime

class Newspaper(Item):
	def __init__(self, id, Is_Secret,page_length,name,item_type,timeobj):

		super().__init__(id)
		
		self.Is_Secret =Is_Secret
		self.page_length = page_length
		self.name = name
		self.item_type=item_type					
		self.timeobj = timeobj
            
	def Item_Type(self):
		return self.item_type
            
   
   # Implementation of the abstract method defined in Class Item
	def Is_Secret(self):
		return self.Is_Secret
		

	def Get_Page_No(self):
		return self._page_length
    
	def SetTime(self,dateime):
		self.timeobj = datetime.datetime
	def GetTime(self):
		return self.timeobj