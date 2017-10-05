from abc import ABC, abstractmethod

""" An abstract class with single attribute: id for each subsequent document classes,
    that will inherit the respective methods and attributes. """



class Item(ABC):
    """ Constructor to intiialize ID"""
    def __init__(self,id):
     self.id = id	
     """ Two abstract methods for Child classes to implement """
    @abstractmethod	
    def Item_Type(self):
        pass

    @abstractmethod
    def Is_Secret(self):
        pass

    def Get_Page_No(self):
        pass

	
             
     
        
	
