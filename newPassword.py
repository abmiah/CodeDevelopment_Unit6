# This scrip will create a new randon password
# Import the required libraries

import random
import string
import hashlib

""" This class generates a new password and prints it to the console. """

class NewPassword:
    def __init__(self):
        self.password = self.random_password()

    """ This function generates a 25-character random password using the "string" library and the 
    @staticmethod decorator as a class method."""
    @staticmethod
    def random_password(length=25):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(characters, k=length))

    def print_password(self):
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        print(f"Please set a new password: \"{self.password}\". Encrypted password: \"{hashed_password}\"")


if __name__ == "__main__":
    password = NewPassword()
    password.print_password()
