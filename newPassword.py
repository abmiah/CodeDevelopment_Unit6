# This scrip will create a new randon password
# Import the required libraries

import random
import string
import hashlib

"""The NewPassword class generates an 18-character password with letters, digits, and punctuation. The "random_password"
 method creates the password, while "print_password" displays it and its hashed value."""


class NewPassword:
    def __init__(self):
        self.password = self.random_password()

    """This function generates a random password with a length of 25 characters. It uses the string library to get 
    the @staticmethod decorator to make it a class method."""
    @staticmethod
    def random_password(length=25):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(characters, k=length))

    """The function below prints the password and its hashed value to the console."""
    def print_password(self):
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        print(f"Please set a new password: \"{self.password}\". Encrypted password: \"{hashed_password}\"")


if __name__ == "__main__":
    password = NewPassword()
    password.print_password()
