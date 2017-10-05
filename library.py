from person import Person
from government_document import Government_Document
from map import Map
from newspaper import Newspaper
import datetime
import time
from datetime import timedelta

class Dummy():
    def __init__(self, item_list, documents,user,log_list,dummyvar,userlist,timeobject):
        self.item_list = item_list # Library inventory list
        self.documents = documents
        self.user_object = user 
        self.loglist= log_list # User checked out item list
        self.dummy_item=dummyvar
        self.userlist = userlist # registered user list
        self.timeobject = timeobject
        
    """ CheckoutItem note: Number of times CheckoutItem invoked must be equal to items added to the library instance """        
    
    def CheckoutItem(self,document_to_check,person,checkout_time):
        for users_userlist in self.userlist:
            if users_userlist.name == person.name:
                for list_in_items in self.item_list: # If items in library inventory match provided document
                    if list_in_items.id == document_to_check.id: # Remove documents since already  present in the list
                    
                        print ("Item", list_in_items.id,"checked out", "by user", users_userlist.name, "at time:",checkout_time.now())
                        temp_var = "Item", list_in_items.id,"checked out", "by user", users_userlist.name, "at time:",checkout_time.now()
                        temp_var = str(temp_var)
                        
                        self.item_list.remove(list_in_items) # Remove from library inventory (item_list)
                        self.loglist.append(list_in_items)# Add list_in_items to user list
                        self.dummy_item = list_in_items
                        self.checkout_log = open("CheckoutLog.txt","a")
                        self.checkout_log.write(temp_var+"\n")
                        self.checkout_log.close()
                        
                    elif list_in_items.id != document_to_check.id:
                        pass # CANNOT TAKE BOOK    
            

    def CheckinItem(self,document_to_putback_to_library,person,checkin_time):
                self.item_list.append(document_to_putback_to_library)
                print ("Item", document_to_putback_to_library.id,"checked in", "by user", person.name, "at time:",checkin_time.now())
                temp_var = "Item", document_to_putback_to_library.id,"checked in", "by user", person.name, "at time:",checkin_time.now()
                temp_var = str(temp_var)
                self.loglist.remove(document_to_putback_to_library)
                self.checkin_log = open("CheckinLog.txt","a")
                self.checkin_log.write(temp_var)
                self.checkin_log.close()
    def ShowInventory(self):
        print("Current library inventory ... ")
        for items_in_inventory in self.item_list:
            if len(self.item_list) !=0:
                print( "ID: ", items_in_inventory.id,"|", " Item Type:", items_in_inventory.Item_Type(),"|","Page length: ",items_in_inventory.page_length,"|"," Is File secret ",items_in_inventory.Is_Secret)

        if len(self.item_list)==0:
                print("Inventory empty!") 
        
    def AddItem(self,item_to_add_library):
        print(item_to_add_library.Item_Type()," with ID:",item_to_add_library.id, "added to the library at time:", item_to_add_library.GetTime() )
        self.item_list.append(item_to_add_library)
        
    def RemoveItem(self,item_id):
        for items_in_inventory in self.item_list:
            if items_in_inventory.id == item_id:
                self.item_list.remove(items_in_inventory)
                
    """ objects have same id but can change other attrs by provind another object of same ID """
    def UpdateItem(self,item_to_update):
        for items in self.item_list:
            if items.id == item_to_update.id:
                items.Is_Secret = item_to_update.Is_Secret
                items.name = item_to_update.Is_Secret
                items.page_lengtht = item_to_update.Is_Secret
                print("Item:",items.id, "updated with name ",items.name," page length",items.page_length)
            else:
               print("Cannot update items that do not exist within the library inventory!")
#                    
#                   print ("Cannot replace inventory as item to substitute not found!")
#        elif len(self.item_list ==0): 
#            print("Cannot update an empty inventory")    

    def ViewUserInfo(self,RegisteredUser):
        
        for items in self.userlist:
            if items.name == RegisteredUser.name:
                print("User: ",RegisteredUser.name , "has the following item/s",self.dummy_item.item_type)
            else:
                pass

    def SetRegisterUser(self,new_user_object): 
           self.user_object = new_user_object
           self.userlist.append(self.user_object)

           print("User registered:",self.user_object.name,"at time:",self.user_object.GetTime())
        
    
        
    def GetRegisterUser(self):
        return self.user_object
        
        
    def Write_LibraryItems_To_File(self):
        #CURRENT_Directory = os.getcwd()
        
        self.file_items = open('LibraryItemList.txt','a')
        for items in self.item_list:
            self.file_items.write("Below are the list of items within the Library inventory at present \n")
            self.file_items.write("Item ID: "+str(items.id)+" |"+" Type "+str(items.Item_Type())+":"+" |"+" Name: "+str(items.name)+ " |"+" Page count: "+str(items.page_length)) 
            
        self.file_items.close()
        
        
    def Write_UserItems_To_File(self,user_to_check):
        #CURRENT_Directory = os.getcwd()
        
        self.file_items = open('UserItemList.txt','a')
        for items in self.userlist:
            if items.name == user_to_check.name:
                self.file_items.write("Below are the list of items carried by library account holders at present \n")
                self.file_items.write("User: "+str(items.name)+"|"+" Item ID: "+str(self.dummy_item.id)+" |"+" Type "+str(self.dummy_item.item_type)+":"+" |"+" Name: "+str(self.dummy_item.name)+ " |"+" Page count: "+str(self.dummy_item.page_length))
                #print("User: ",user_to_check.name , "has the following document/s",self.dummy_item.item_type)
            else:
                pass
            
        self.file_items.close()
        
        
        
    
    
    """  Note:
         DeleteUser Method.
         Users cannot be removed unless user item list is empty i.e no outstanding dues
        
    """ 
    
    def DeleteUser(self,user_to_delete):
        for registeredusers in self.userlist:
            if isinstance((user_to_delete.name), int):
                return ("You have entered an invalid User name. It must be a string.")
            #print(registeredusers.name)
            #print(user_to_delete.name)
            if user_to_delete.name == registeredusers.name:
                    if len(self.loglist) != 0:
                            return ("Cannot remove accounts due to loans in the User Account")
                    elif len(self.loglist) == 0:
                        del(registeredusers)
                        return "Deleted user account: "+ str(user_to_delete.name)
                        

    def SetMakeTime(self,Time_Item_Created):
        
        self.Time_difference = Time_Item_Created- self.timeobject
        #datetime.timedelta()
        self.Time_difference = self.Time_difference
        
    def GetMakeTime(self):
        return self.Time_difference
        
        
"""  Simulated start time of the library. i.e Opening time"""
TimeObj = datetime.datetime
print("Library opening time: ",TimeObj.now())
print("\n")
""" Instantiate the library class with dummy paramters. """
MyLibrary = Dummy([],Newspaper(1,True,10,"Dummy","",TimeObj),Person("dummy",TimeObj),[],[],[],TimeObj.now())


"""  Pointer variables to prevent object memory conflict """
mapToAdd1 = Newspaper(1,True,10,"TheGuardian","Tabloid",TimeObj.now())

""" Two seconds interval gap of creating the items.
    Note: Assume items added to the library inventory after every two seconds. """

time.sleep(2)
mapToAdd2 = Map(32,True,"Anchorage_1",1,"Map",TimeObj.now()) 
time.sleep(2)
mapToAdd3 = Map(10,True,"Manchester",1,"Map",TimeObj.now()) 
time.sleep(2)
mapToAdd4 = Map(10,False,"Birmingham",1,"Map 2",TimeObj)
time.sleep(2)
mapToAdd4 = Government_Document(10,False,39,"HMRC",TimeObj)



"""Add an item to library inventory """
MyLibrary.AddItem(mapToAdd1)

"""Add an item to library inventory """
MyLibrary.AddItem(mapToAdd2)
MyLibrary.AddItem(mapToAdd3)
"""Add an item to library inventory """
print("\n")


""" Show content of the library inventory """
MyLibrary.ShowInventory()

""" Delay user creation by two seconds as done above. """
time.sleep(2)
mapToAddName1 = Person("XYZ",TimeObj.now())
time.sleep(2)
mapToAddName2 = Person("Rambo",TimeObj.now())
time.sleep(2)
mapToAddName3 = Person("Kevin Spacey",TimeObj.now())


""" Register three users """
MyLibrary.SetRegisterUser(mapToAddName1)
MyLibrary.SetRegisterUser(mapToAddName2)
MyLibrary.SetRegisterUser(mapToAddName3)

print("\n")

""" Delete user: mapToAddName3 """

MyLibrary.DeleteUser(mapToAddName3)

#
#
print("\n")

""" Checkout an item to person inventory"""
time.sleep(2)
Checkout_time_object1 = datetime.datetime
MyLibrary.CheckoutItem(mapToAdd1,mapToAddName1,Checkout_time_object1)
""" Show content of the library inventory"""
MyLibrary.ShowInventory()

print("\n")
time.sleep(2)
Checkout_time_object2 = datetime.datetime
""" Checkout (Take out) an item onto person inventory"""
MyLibrary.CheckoutItem(mapToAdd2,mapToAddName2,Checkout_time_object2)

""" Checkout an item onto person inventory"""
time.sleep(2)
Checkout_time_object3= datetime.datetime

MyLibrary.CheckoutItem(mapToAdd3,mapToAddName2,Checkout_time_object3)
print("\n")
time.sleep(5)
Checkin_timeobject1 = datetime.datetime
""" Checkin (Put in) an item onto person inventory"""

MyLibrary.CheckinItem(mapToAdd3,mapToAddName2,Checkin_timeobject1)

""" Write library inventory items to a text file """
MyLibrary.Write_LibraryItems_To_File()

""" Write user data to a text file """
MyLibrary.Write_UserItems_To_File(mapToAddName1)

""" View user inventory"""
MyLibrary.ViewUserInfo(mapToAddName1)
""" Update an item existing within the library inventory"""
MyLibrary.UpdateItem(mapToAdd4)
""" Show content of the library inventory"""
MyLibrary.ShowInventory()


