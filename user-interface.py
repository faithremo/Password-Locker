from user import user, userCredentials

function()

def create_newUser(username, password):
    """This is a function that creates a new user with a username and password.
    """
    newUser = user(username, password)
    return newUser

def saveUser(user):
    """This function saves a new user
    """
    user.saveUser()

def displayUser():
    """This function displays an existing user
    """
    return user.displayUser()

def loginUser(username, password):
    """This function checks if a user exists then the user is loggedin
    """
    checkUser = userCredentials.userVerification(username, password)
    return checkUser

def create_newCredential(accountName, username, password):
    """This function creates new credentials for a given user account
    """
    newCredential = userCredentials (accountName, username, password)
    return newCredential

def save_credentials(credentials):
    """This function saves credentials to the list of credentials
    """
    credentials.saveDetails()
    
def display_accountsDetails():
    """This function returns all the credentials that have been saved by the user
    """
    return userCredentials.displayCredentials()

def delete_credential(credentials):
    """This function deletes an extisting credential from the list of credentials"""
    credentials.deleteCredentials()
    
def find_credential(accountName):
    """THis function searches for an account name credential and returns the credentials for that account
    """
    return userCredentials.findCredentials(accountName)