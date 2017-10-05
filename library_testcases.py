import unittest
from library import Dummy
from person import Person
from government_document import Government_Document
from map import Map
from newspaper import Newspaper
import datetime
import time
class LibraryTestCases(unittest.TestCase):
    
    def setUp(self):
        TimeObj = datetime.datetime

        self.LibraryObject = Dummy([],Newspaper(1,True,10,"Dummy","",TimeObj),Person("dummy",TimeObj),[],[],[],TimeObj.now())
              
        
        
    """ Firstly, run a test on the user registration method,
        to ensure right Name string is being fed. """        
        
    def test_Check_RegisteredUser(self):
        TimeObj = datetime.datetime
        self.LibraryObject.SetRegisterUser(Person("XYZ",TimeObj.now()))
        Registered_User = self.LibraryObject.GetRegisterUser()
        self.assertIs(Registered_User.name,"XYZ")
    
    """ Up to this point we expect Library to have no documents,
        as we haven't used AddItem Method, yet. """
        
    def test_Check_If_Library_List_Empty(self):
        Library_list_length = len(self.LibraryObject.item_list)
        self.assertIsNot(Library_list_length,1)
        
        
        
    """ Now verify that the library indeed has a document item."""        
        
        
        
    def test_Check_If_Library_List_Not_Empty(self):
        TimeObj = datetime.datetime

        self.LibraryObject.AddItem(Newspaper(1,True,10,"theGuardian","Tabloid",TimeObj.now()))
        Library_list_length = len(self.LibraryObject.item_list)
        self.assertIs(Library_list_length,1)
    
    """ Test cases for the Check-in conditions """
    
    """ Condition(1): If book available in the Library inventory, and matches to the checkout item,
                          then remove it from library """ 
     
    """ CheckoutItem note: Number of times CheckoutItem invoked must be equal to items added to the library instance """        
                     
    def test_Checkout_Method_Case_Book_Available_in_Library(self):
        TimeObj = datetime.datetime

        mapToAdd1 = Newspaper(1,True,10,"theGuardian","Tabloid",TimeObj.now()) 

        mapToAddName1 = Person("XYZ",TimeObj.now())

        self.LibraryObject.SetRegisterUser(mapToAddName1)
      
        
        self.LibraryObject.AddItem(mapToAdd1)
                
        self.LibraryObject.CheckoutItem(mapToAdd1,mapToAddName1,TimeObj.now())
        self.assertEqual(len(self.LibraryObject.item_list),0) 



    
    def test_Checkout_Method_Case_Book_Not_Available_in_Library(self):
        """ Condition(2): If book NOT available in the Library inventory,
                          then no book can be removed """
        TimeObj = datetime.datetime
            
        self.LibraryObject.AddItem(Newspaper(2,True,10,"theGuardian","Tabloid",TimeObj.now()))
        mapToAddName1 = Person("XYZ",TimeObj.now())
        
        self.LibraryObject.CheckoutItem(Newspaper(1,True,10,"theGuardian","Tabloid",TimeObj.now()),mapToAddName1,TimeObj.now())
        for item_in_library_inventory in self.LibraryObject.item_list:
            """ Assertion: item_in_library_inventory.id == 2, Check-out item id == 1 """
            self.assertNotEqual(item_in_library_inventory.id,1)
        
        
        """ Check in method places rented documents back to the library inventory"""
    def test_on_CheckIn_Method(self):
        TimeObj = datetime.datetime

        mapToAdd1 = Newspaper(1,True,10,"TheGuardian","Tabloid",TimeObj.now()) 
        mapToAddName2 = Person("Rambo",TimeObj.now())
        
        self.LibraryObject.SetRegisterUser(mapToAddName2)
        self.LibraryObject.AddItem(mapToAdd1)
        self.LibraryObject.CheckoutItem((mapToAdd1),mapToAddName2,TimeObj.now())
      
        """ Assertion: Library inventory now has a document checked out.
            Inventory empty since the only one added item was checked out"""
        time.sleep(3)
        self.assertIs(len(self.LibraryObject.item_list),0)
        Checkin_timeobject1 = datetime.datetime

        self.LibraryObject.CheckinItem(mapToAdd1,mapToAddName2,Checkin_timeobject1)
        
        """ Assertion: Library inventory now has a document checked in. """
        self.assertEqual(len(self.LibraryObject.item_list),1)
        
        """ Note on the DeleteUser conditions.
            
           (i) To delete a User Account, we must feed in a string only else throw an exception.
               Since the user Class has only two attributes, name and user_list
               
           (ii) Also, cannot delete a User account with overdue items
            

        """
    
    
    def test_Check_DeleteUser(self):
        TimeObj = datetime.datetime
        """ Case(i) string name provided """        
        
    
        """ Assume Library has two items """
        mapToAdd1 = Newspaper(1,True,10,"theGuardian","Tabloid",TimeObj.now()) 
        mapToAddName1 = Person("Rambo",TimeObj.now())
        mapToAddName2 = Person("John",TimeObj.now())
        
        """ Set user """
        self.LibraryObject.SetRegisterUser(mapToAddName1)
        self.LibraryObject.SetRegisterUser(mapToAddName2)        
        time.sleep(2)
        Checkout_time = datetime.datetime
        """ Loan out a book to the user """
        self.LibraryObject.CheckoutItem(mapToAdd1,mapToAddName1,Checkout_time)
        
        """ Deleting the above account which actually owes a book to the library
            will result in a string being thrown out. """
        
        Return_String = self.LibraryObject.DeleteUser(mapToAddName1)
        
        self.assertEqual(Return_String,'Deleted user account: Rambo')
        
        
        """Case(ii) invalid name provided to DeleteMethod """
        
        """ Assume Library has two items """
        mapToAdd1 = Newspaper(1,True,10,"theGuardian","Tabloid",TimeObj.now()) 
        mapToAddName1 = Person(1,TimeObj.now())
        mapToAddName2 = Person("John",TimeObj.now())
        
        """ Set user """
        self.LibraryObject.SetRegisterUser(mapToAddName1)
        self.LibraryObject.SetRegisterUser(mapToAddName2)        

        
        """ Loan out a book to the user """
        self.LibraryObject.CheckoutItem(mapToAdd1,mapToAddName1,Checkout_time.now())
        
        
        Return_String = self.LibraryObject.DeleteUser(mapToAddName1)
        
        self.assertEqual(Return_String,'You have entered an invalid User name. It must be a string.')
        
    
        """Test to check if items are being deleted in the library inventory"""
        
        
    def test_DeleteItem(self):
        TimeObj = datetime.datetime

        self.assertTrue(len(self.LibraryObject.item_list) == 0)
        
        
        mapToAdd1 = Newspaper(2,True,10,"theGuardian","Tabloid",TimeObj.now()) 
        
        
        self.LibraryObject.AddItem(mapToAdd1)
        """ Verify whether item has been added"""
        self.assertTrue(len(self.LibraryObject.item_list) != 0)        
        
        """ Delete user_object from library  """
        self.LibraryObject.RemoveItem(mapToAdd1.id)
        
        print(self.LibraryObject.item_list)
        
        """ Verify whether item has been removed from library """
        self.assertTrue(len(self.LibraryObject.item_list) == 0)
        

if __name__ == '__main__':
    unittest.main()        
    