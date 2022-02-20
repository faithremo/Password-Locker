from user import user, userCredentials


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
    print("Hello, Welcome to your Password Locker.")
    print('*' * 40)
    print('-' * 40)
    
    print("To proceed, please enter: \n 1 --- To Create a new account  \n 2 --- To Login if you have an account  \n")
    
    short_code = input("").lower().strip()
    if short_code == "1":
        print("\nSign Up")
        print('=' * 40)
        username = input("Input your User Name:")
        while True:
            print("Enter: \n 1 --- To type your own password;\n 2 --- To generate a random password\n\n")
            chosen_password = input().strip()
            if chosen_password == "1":
                password = input("Please enter password\n")
                break
            elif chosen_password == "2":
                password = generatePassword()
                break
            else:
                print("Invalid input. Please try again!!!\n")
            
        saveUser(create_newUser(username, password))
        print("="*60)
        print(f"Hello {username},\n Your account has been created successfully!\n Your password is: {password}")
        print("="*60)
        
    elif short_code =="2":
        print("=" * 50)
        print("Please enter your User name and Password to Login:\n")
        print("=" * 50)
        username = input("Input your User Name:")
        password = input("Input your Password:")
        login = loginUser(username, password)
        if loginUser == login:
            print(f"Hello {username}. Welcome to Password Locker. \n")
        
    while True:
        print("\nSelect a number for the service you need below:\n 1 - Create a new credential \n 2 - Display credential \n 3 - Find a credential \n 4 - Delete a credential \n 5 - Generate a random password \n 0 - Exit the application \n \n")
        short_code = input().strip()
        if short_code == "1":
            print("Create a new credential")
            print("*" * 25)
            print("Account name:")
            account =input()
            print("\nYour Account username:")
            user_name = input()
            while True:
                print("\nInput:\n 1 -- To type your own password you have an existing account;\n 2 -- To generate a random password\n")
                chosen_password = input().strip()
                if chosen_password == '1':
                    password = input("\nEnter your password:\n")
                    break
                elif chosen_password == '2':
                    password = generatePassword()
                    break
                else:
                    print("Invalid input. Please try again!!!")
            
            save_credentials(create_newCredential(account, username, password))
            print(f"\n Your - {account} - Account credentials containing:\n Username: {username} -and - Password: {password}\n have been created successfully.\n")
        elif short_code == "2":
            if display_accountsDetails():
                print ("Here is a list of your accounts:\n")
                
                print("="* 30)
                print("\n")
                for accountName in display_accountsDetails():
                    print(f"Account name: {accountName.accountName} \n Username: {username}\n Password: {password}")
                    print("="* 30)
                print("\n")
            else:
                print("You do not have any credentials saved yet!!!\n")
        elif short_code == "3":
            print("\nEnter the Account name to search for its credentials.\n")
            search_name = input()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"\n Account name: {search_credential.accountName}")
                print("-" *40)
                print(f"User name: {search_credential.username} \nPassword: {search_credential.password}")
                print("-" *40)
            else:
                print("The credential you are searching for does not exist!!!\n")
        elif short_code == "4":
            print("\nEnter the account name of the credentials you want to delete.\n")
            search_name = input().capitalize()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("=" * 30)
                search_credential.delete_credential()
                print(f"\n Your {search_credential.accountName} account credentials have successfully been deleted!!! \n")
            else:
                print("The credential you want to delete does not exit in your storage.\n")
                
        elif short_code == "5":
            password = generatePassword()
            print(f"\nYour password --{password}-- has been generated successfully.\n")
        elif short_code == "0":
            print("\nThank you for using Password Locker... See you soon!\n")
            break
        else:
            print("\nWrong entry...Please choose an entry that matches those in the menu\n")
    else:
        print("\nPlease enter a valid input to proceed.\n")
        

if __name__ == "__main__":
    password_locker()