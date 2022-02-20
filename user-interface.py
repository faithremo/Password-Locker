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
    """This function searches for an account name credential and returns the credentials for that account
    """
    return userCredentials.findCredentials(accountName)

def check_credentials(accountName):
    """This function confirms if a credential exists with that account name and either returns true or false
    """
    return userCredentials.if_credential_exists(accountName)

def generatePassword():
    """This function generates a random user password
    """
    random_password = userCredentials.generate_user_password()
    return random_password

def password_locker():
    print("Hello, Welcome to your Password Locker. \n To proceed, please enter: \n 1 --- To Create a new account  \n 2 --- To Login if you have an account  \n")
    short_code = input("").lower().strip()
    if short_code == "1":
        print("Sign Up")
        print('=' * 40)
        username = input("Input your User Name:")
        while True:
            print("Enter: \n 1 --- To type your own account;\n 2 --- To generate a random password")
            chosen_password = input().lower().strip()
            if chosen_password == "1":
                password = input("Please enter password\n")
                break
            elif chosen_password == "2":
                password = generatePassword()
                break
            else:
                print("Invalid input. Please try again!!!")
            
        saveUser(create_newUser(username, password))
        print("="*90)
        print(f"Hello {username}, Your account has been created successfully! Your password is: {password}")
        print("="*90)
        
    elif short_code =="2":
        print("=" * 40)
        print("Please enter your User name and Password to Login:")
        print("=" * 40)
        username = input("Input your User Name:")
        password = input("Input your Password:")
        login = loginUser(username, password)
        if loginUser == login:
            print(f"Hello {username}. Welcome to Password Locker. \n")
        
    while True:
        print("Select a number for the service you need below:\n 1 - Create a new credential \n 2 - Display credential \n 3 - Find a credential \n 4 - Delete a credential \n 5 - Generate a random password \n 0 - Exit the application \n \n")
        short_code = input().strip()
        if short_code == "1":
            print("Create a new credential")
            print("*" * 20)
            print("Account name:")
            account =input().capitalize()
            print("Your Account username:")
            user_name = input()
            while True:
                print("Input:\n 1 -- To type your own password you have an existing account;\n 2 -- To generate a random password")
                chosen_password = input().strip()
                if chosen_password == '1':
                    password = input("Enter your password:\n")
                    break
                elif chosen_password == '2':
                    password = generatePassword()
                    break
                else:
                    print("Invalid input. Please try again!!!")
            
            save_credentials(create_newCredential(accountName, username, password))
            print(f"\n Your {accountName} Account credentials containing: Username: {username} -and - Password: {password} have been created successfully.\n")
        elif short_code == "2":
            if display_accountsDetails():
                print ("Here is a list of your accounts:")
                
                print("="* 30)
                print("\n")
                for accountName in display_accountsDetails():
                    print(f"Account name: {accountName.accountName} \n Username: {username}\n Password: {password}")
                    print("="* 30)
                print("\n")
            else:
                print("You do not have any credentials saved yet!!!")
        elif short_code == "3":
            print("Enter the Account name to search for its credentials.")
            search_name = input()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account name: {search_credential.accountName}")
                print("-" *40)
                print(f"User name: {search_credential.username} \nPassword: {search_credential.password}")
                print("-" *40)
            else:
                print("The credential you are searching for does not exist!!!\n")
        elif short_code == "4":
            print("Enter the account name of the credentials you want to delete.")
            search_name = input().capitalize()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("=" * 30)
                search_credential.delete_credential()
                print(f"\n Your {search_credential.accountName} account credentials have successfully been deleted!!! \n")
            else:
                print("The credential you want to delete does not exit in your storage.")
                
        elif short_code == "5":
            password = generatePassword()
            print(f"Your password --{password}-- has been generated successfully.")
        elif short_code == "0":
            print("Thank you for using Password Locker... See you soon!")
            break
        else:
            print("Wrong entry...Please choose an entry that matches those in the menu")
    else:
        print("Please enter a valid input to proceed.")
        

              
            
                
            
            
            

