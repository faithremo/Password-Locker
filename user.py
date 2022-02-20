from operator import truediv
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
        
        accountUser=""
        for User in user.userList:
            if (User.username == username and User.password == password):
                accountUser == User.username
        return accountUser
    
    def __init__(self, accountName, username, password):
        """This method defines the user credentials that will be stored.
        """
        self.accountName=accountName
        self.username=username
        self.password=password
        
    def saveDetails(self):
        """This method stores a new credential to our list of credentials.
        """
        userCredentials.credentialsList.append(self)
        
    def deleteCredentials(self):
        """This method deletes an existing account credentials from the list of credentials
        """
        userCredentials.credentialsList.remove(self)
        
    @classmethod
    def findCredentials(cls, accountName):
        """This method uses the account name you are searching for and returns the credentials of the account name saved.
        """
        for credential in cls.credentialsList:
            if credential.accountName == accountName:
                return credential
    
    @classmethod
    def if_credential_exists(cls, accountName):
        """This method confirms if a credential exists from the credentials list and returns true or false
        """
        for credential in cls.credentialsList:
            if credential.accountName == accountName:
                return True
        return False
    
    @classmethod
    def displayCredentials(cls):
        """This method displays content in the credentials list
        """
        return cls.credentialsList
    
    def generate_user_password(stringLength=8):
        """this method will generate a random password string containing digits, letters and special characters
        """
        password = string.digits + string.ascii_lowercase +string.ascii_uppercase + "!~@$#%&|^*"
        return ''.join(random.choice(password) for i in range(stringLength))