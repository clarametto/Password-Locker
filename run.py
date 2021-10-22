from user import User

# from user import User
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


def create_credentails(user_name, name, password):

    '''
    Function to create a credential 
    Args:
        user_name: username for Password Locker
        name: name of the account 
        password: associated password for the account
    '''


    new_credentails = Credentials(user_name, name, password)

    return new_credentails


def save_credentials(credentials):

    '''
    Function to save credentials
    Args:
        credentials: credentials to be saved
    '''

    credentials.save_credentials()


def check_existing_credentials(name):

    '''
    Function that checks existence of user credentials
    Args:
        name: credentials name
    '''

    return Credentials.credentials_exists(name)


def display_credentials(password):

    '''
    Function that returns all the saved credentials
    '''

    return Credentials.display_credentials(password)


def create_generated_password(name):

    '''
    Function that generates a password for the user 
    Args:
        name : the name of the account
    '''


    password = Credentials.generated_password()

    return password


def find_credentials(credentials_name, credentials_password):
    
    '''
    Function to find credentials based on credentials name given
    '''


    return Credentials.find_credentials(credentials_name, credentials_password)


def delete_credentials(name):
    
    '''
    Function to delete credentials
    Args:
        name: name of credentials
    '''


    Delete = Credentials.delete_credentials()

     

#my main function
def main():
    '''
    function that will run password locker application

    '''
    while True:
        '''
        looping through the entire application
        '''

        print("""Short codes to select: 
        ca = Create Account: password locker
        ds = display name and details of the user
        lg = login your account
        exit = exit password locker application """)

        short_code = input().lower()


        if short_code == "ca":
            '''
            creating user account
            '''

            print("\n")
            print("Your new password locker account: ")
            print("*"*8)
            print("Enter username: ")
            user_name = input()

            print("Create password: ")
            user_password = input()

            #saving user inputs
            save_users(create_user(user_name, user_password))

            print("\n")
            print(f"Hello {user_name} \n Your account have been created successfully. \n Welcome !!!  \n You can now write LG to login. \n")


        elif short_code == "ds":
            '''
            displays user names and details
            '''
            if display_users():
                print("\n")
                print("#"*20)
                print("Below is a list of current users prt\n")

                for user in display_users():
                    print(f"{user.user_name}")
                    print("*"*20)

            else:
                print("\n")
                print("No user found in Password locker. \n Write CA to create yours. ")
                print("\n")
                
        
        # elif short_code == "lo":
        # elif short_code == "exit":
        # else





  
if __name__ == '__main__':
    main()


    