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

    def save_credentials(self):
        '''
        method helps to save credentials in credentials_list
        '''
        Credentials.credentials_list.append(self)
        
    @classmethod
    def generated_password(cls):
        '''
        method that generate rondom password for user
        '''


        #length of password to be generated
        pass_length = 8 

        #random characters to chosen, alpha numeric
        alpha_num = string.ascii_uppercase + string.ascii_lowercase + string.digits

        password = "".join(choice(alpha_num) for index in range(pass_length))
        return password


    @classmethod
    def display_credentials(cls, user_name):
        
        '''
        Method that  returns credentials_list
        Args:credentials_email: the email of the credentials account
            password: user password
        '''


        user_credentials_list = []

        for credentials in cls.credentials_list:
            if credentials.user_name == user_name:
                user_credentials_list.append(credentials)

        return user_credentials_list

    
    
    @classmethod
    def credentials_exists(cls, credentials_name):
        
        '''
        Method to check if credentials exists
        Args
            name: name of credentials to be searched
        Returns:
            Boolean: True or False
        '''



        for credentials in cls.credentials_list:
            if credentials.credentials_name == credentials_name:
                return True

        return False

    
    
    

if __name__ =='__main__':
    unittest.main()


    
