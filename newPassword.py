# This scrip will create a new randon password

import random
import string
import hashlib

class NewPassword:
    def __init__(self):
        self.password = self.random_password()


    @staticmethod
    def random_password(length = 18):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(characters, k=length))

    def print_password(self):
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        print(f"The new password is: {self.password}. Hashed is: {hashed_password}")


if __name__ == "__main__":
    password = NewPassword()
    password.print_password()

