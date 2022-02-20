from user import user, userCredentials

function()

def create_newUser(username, password):
    """This is a function that creates a new user with a username and password.
    """
    newUser = user(username, password)
    return newUser