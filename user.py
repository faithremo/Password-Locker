import string
import random

class user:
    """creating a user class to allow genarartion of new instances of a user.
    """
    user_list = []
     
    def __init__(self,username,password):
         
         """this method outlines the properties of a user.
         """
         self.username = username
         self.password = password
    
    