import unittest
from user import user
from user import userCredentials

class test_class(unittest.test_case):
    """
    This is a test class that defines test cases for the user class.
    """
    def setUp(self):
        """
        This method runs before each test methods run.
        """
        self.newUser = user('faithremo','1234')

    def test_init(self):
        """
        This is a test case that checks if the object has initialized correctly
        """
        self.assertEqual(self.newUser.username,'faithremo')
        self.assertEqual(self.new_user.password,'1234')

    def test_saveuser(self):
        """
        This is a test case to test if a new user instance has been saved into the list of users
        """
        self.newUser.saveUser()
        self.assertEqual(len(user.userList),1)

class test_credentials(unittest.test_case):
    """
    This class that defines test cases for credentials class
    """ 
    def set_up(self):
        """
        This method runs before each credentials test methods that are run.
        """
        self.newCredential = userCredentials('Gmail','faithmakumi','1234')
    def test_init(self):
        """
        This is a test case that checks if a new userCredentials instance has been initialized correctly
        """
        self.assertEqual(self.newCredential.accountName,'Gmail')
        self.assertEqual(self.newCredential.username,'faithmakumi')
        self.assertEqual(self.newCredential.password,'1234')

    def save_credentialtest(self):
        """
        This test case testst if the credential object is saved into the list of credentials
        """
        self.newCredential.saveDetails()
        self.assertEqual(len(userCredentials.credentialsList),1)

    def cleanUp(self):
        '''
        This method cleans up after each test case has run.
        '''
        userCredentials.credentialsList = []

    def test_save_multiple_accounts(self):
        '''
        This test checks if we can save many credentials objects to our list of credentials
        '''
        self.newCredential.saveDetails()
        test_credential = userCredentials("Twitter","faithmakumi","1234") 
        test_credential.saveDetails()
        self.assertEqual(len(userCredentials.credentialsList),2)

    def test_deleteCredential(self):
        """
        This test method to test if an account credentials can be deleted from the list of credentials
        """
        self.newCredential.saveDetails()
        test_credential = userCredentials("Twitter","faithmakumi","1234")
        test_credential.saveDetails()

        self.newCredential.deleteCredentials()
        self.assertEqual(len(userCredentials.credentialsList),1)

    def test_search_credentials(self):
        """
        This test searches for a credential already saved by account name and returns the details of the credential
        """
        self.newCredential.saveDetails()
        test_credential = userCredentials("Twitter","faithmakumi","1234") 
        test_credential.saveDetails()

        theCredential = userCredentials.findCredentials("Twitter")

        self.assertEqual(theCredential.account,test_credential.accountName)

    def test_credentialExist(self):
        """
        This test confirms if a true or false can be returned based on whether the credential can be found.
        """
        self.newCredential.saveDetails()
        theCredential = userCredentials("Twitter", "faithmakumi", "1234")  
        theCredential.saveDetails()
        credential_is_found = userCredentials.if_credential_exists("Twitter")
        self.assertTrue(credential_is_found)

    def test_displayAllSavedCredentials(self):
        '''
        This method displays all the credentials that the user has saved
        '''

        self.assertEqual(userCredentials.displayCredentials(),userCredentials.credentialsList)
        
        