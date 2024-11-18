# This is section of the code will check the admin password and test to see if it has been encrypted or not
# The code will use the hashlib library to hash the password

import hashlib
from adminPassword import AdminPassword

"""The inital class will set the admin password and hash it using the hashlib library"""
class PasswordHash:
    def __init__(self, admin_password):
        self.admin = admin_password
        self.hashed_password = self.hash_password(self.admin.password)

    """The function below encrypted the password using sha256. The password is then encoded and hashed"""
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    """The function below checks if the password is hashed or not"""
    def is_password_hashed(self, password):
        return password == self.hashed_password

    """The part of the function below will print the hashed password to the console"""
    def print_hashed_password(self):
        print(f"The hashed password is: {self.hashed_password}")

if __name__ == "__main__":
    hasher = PasswordHash()
    hasher.print_hashed_password()

    """The code below simply checks if the password is hashed or not and prints the result to the console, 
    this should be commented out in the final code"""
    # if hasher.is_password_hashed(hasher.admin.password):
    #     print(f"The password {hasher.admin.password} is hashed")
    # else:
    #     print(f"The password {hasher.admin.password} is not hashed")



