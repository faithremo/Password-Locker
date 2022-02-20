import string
import random

class user:
    """creating a user class to allow genarartion of new instances of a user.
    """
    userList = []
     
    def __init__(self,username,password):
         
         """this method outlines the properties of a user.
         """
         self.username = username
         self.password = password
         
         
    def saveUser(self):
        """this method saves a new user intance in to the user list.
        """
        user.userList.append(self)
        
    @classmethod
    def displayUser(cls):
        return cls.userList
    
    def deleteUser(self):
        """This method deleted a saved account from the list
        """
        user.userList.remove(self)
        
    
class userCredentials():
    """create a credentials class that will enable creation of new objects of credetials
    """
    
    credentialsList = []
    
    @classmethod
    def userVerification(cls, username, password):
        """This is method verifies if the user is in our user list or not
        """