import unittest
from credentials import Credentials 

class User:
    '''
    class that generates new instance of user

    '''

    user_list = []  # it will save new users

    def __init__(self, user_name, user_password):
        '''
        __init__ method defines the properties of user object
        Args: 
            user_name = username of user
            user_password =password user
        '''

        self.user_name = user_name
    

    def save_user(self):
        '''
        it saves new user in the user_list[] above
        '''

        User.user_list.append(self)


        # Find user Credentials

    @classmethod
    def find_credentials(cls, name):
        '''
        it will check correct imports

        Args:
            name: credential name
        Returns:
            Boolean: True/False
        '''

        #search in the user list
        for credentials in Credentials.credentials_list:
            if credentials.credentials_name == name:
                return True

        return False

    @classmethod
    def log_in(cls, name, password):
        '''
        method that allows user to login his/her account
        Args:
            name: name of user
            password: password for user
        returns:
            user credentials: if name and password match
                else:

                    False 
        '''


        for user in cls.user_list:
            if user.user_name ==name and user.user_password ==password:
                return Credentials.credentials_list
            return False

            
    @classmethod
    def  display_user(cls):
        '''
        method that displays user_list
        '''


        return cls.user_list

    

        