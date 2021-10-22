import unittest
from random import choice
import string

from user import User



class Credentials:
    '''
    class that generates instances of user credentials

    '''

    credentials_list = [] # Empty credentials_list
    def __init__(self, user_name, credentials_name, credentials_password):
        '''
        __init__() method it specifies attributes of user credentials object 
        Args:
            user_name:user name 
            credentials_name:name of the credentials account
            credentials_password:associated password

        '''
        self.user_name =user_name
        self.credentials_name = credentials_name
        self.credentials_password = credentials_password
        

    
