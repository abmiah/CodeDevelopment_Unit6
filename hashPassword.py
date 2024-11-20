# This code checks if the admin password is encrypted.
# The code will utilise the hashlib library to hash the password.

import hashlib

"""The initial class will set the admin password and use the hashlib library to hash it."""


class PasswordHash:
    def __init__(self, admin_password):
        self.admin = admin_password
        self.hashed_password = self.hash_password(self.admin.password)

    """The function below encrypts the password using SHA-256. After that, it encodes and hashes the password."""

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    """The function below checks if a password is hashed."""

    def is_password_hashed(self, password):
        return password == self.hashed_password

    """The section of the function below will display the hashed password on the console."""

    def print_hashed_password(self):
        print(f"The hashed password is: {self.hashed_password}")


if __name__ == "__main__":
    hasher = PasswordHash()
    hasher.print_hashed_password()
