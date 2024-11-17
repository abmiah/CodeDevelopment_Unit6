#This is section of the code will check the admin password and test to see if it has been encrypted or not

import hashlib
from adminPassword import AdminPassword

class PasswordHash:
    def __init__(self, admin_password):
        self.admin = admin_password
        self.hashed_password = self.hash_password(self.admin.password)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def is_password_hashed(self, password):
        return password == self.hashed_password

    def print_hashed_password(self):
        print(f"The hashed password is: {self.hashed_password}")

if __name__ == "__main__":
    hasher = PasswordHash()
    hasher.print_hashed_password()

    # if hasher.is_password_hashed(hasher.admin.password):
    #     print(f"The password {hasher.admin.password} is hashed")
    # else:
    #     print(f"The password {hasher.admin.password} is not hashed")



