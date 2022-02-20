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