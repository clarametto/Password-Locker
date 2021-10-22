from user import User
from credentials import Credentials



'''
running my application

'''


def create_user(name, password):
    '''
    Function that creates a user account
    Args
        name: user chosen name
        password: select password for account
    '''

    new_user = User(name, password)

    return new_user


def save_users(user):
    
    '''
    Function to save created user account
    Args
        user: user account to be saved
    '''


    user.save_user()


def check_existing_users(name):

    '''
    Function that checks existence of user account name
    Args:
        name : name of user account
    '''

    return User.user_exist(name)


def user_log_in(name, password):

    '''
    Function that allow users to login their credential account
    Args:
        name : name user used in creating user account
        password: password associated t with user account
    '''


    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)


def display_users():

    '''
    Function that returns all saved users 
    '''


    return User.display_user()

