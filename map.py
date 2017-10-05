from item import Item # Import parent class Item to use id attribute
import datetime
""" Map item is another child class consisting of four attributes:
        Is.Secret: Is the item secret? (Boolean)
        name: Document name
        page_length: Number of pages in the item
        item_type: Dummy variable"""
class Map(Item):
	def __init__(self, id, Is_Secret,name,page_length,item_type,timeobj):
		super().__init__(id) 
		self.name = name
		self.Is_Secret =Is_Secret
		self.name = name 
		self.page_length = page_length
		self.item_type = item_type
		self.timeobj = timeobj
#      """ Implementationn of abstract method defined in Item List """
	def Item_Type(self):
		return self.item_type


	def Is_Secret(self):
		return self.Is_Secret
    
	def SetTime(self,dateime):
		self.timeobj = datetime.datetime
	def GetTime(self):
		return self.timeobj
