# Importing the required modules used for visualising the password check

import threading
import time
from colorama import Fore

# Imported the required files from the other scripts

from adminPassword import AdminPassword
from pwnedPasswordCheck import PwnedURL
from hashPassword import PasswordHash
from passwordCount import PasswordCount
from newPassword import NewPassword

""" The "PasswordChecker" class checks passwords against the NCSC PwnedPasswordsTop100k.txt file, verifies their length, 
hashes them, and generates a new password if weak."""


class PasswordChecker:
    def __init__(self, hub_password):
        self.admin = hub_password
        self.url = PwnedURL()
        self.hasher = PasswordHash(self.admin)
        self.new_random_password = NewPassword()

    """ The "check_password_from_pwned" method verifies if the admin password is in the NCSC PwnedPasswordsTop100k.txt file. """

    def check_password_from_pwned(self):
        password_list = self.url.get_password_list()
        if self.admin.password in password_list:
            print(f"\"{self.admin.password}\" Password is listed in NCSC PwnedPasswordsTop100k.txt")
        else:
            print(f"\"{self.admin.password}\" Password is not listed in NCSC PwnedPasswordsTop100k.txt")

    """ The function verifies if the admin password is encrypted using the "is_password_hashed" method from the 
    "PasswordHash" class."""

    def check_password_hashed(self):
        if self.hasher.is_password_hashed(self.admin.password):
            print(f"The password \"{self.admin.password}\" is hashed")
        else:
            print(f"The password \"{self.admin.password}\" is not hashed. \"{self.admin.password}\" as hashed \"{self.hasher.hashed_password}\"")

    """ The function verifies the length of the password and the types of characters used by using the 
    "PasswordCount" class. """

    def check_password_length(self):
        password_count = PasswordCount(self.admin)
        password_count.print_password_length()
        password_count.print_character_types()
        password_count.print_password_strength()

    """ The "new_password" method evaluates password strength and generates a new one if it is weak. """

    def new_password(self):
        password_count = PasswordCount(self.admin)
        if password_count.is_password_weak():
            self.new_random_password.print_password()
        else:
            print(Fore.GREEN + "No mitigation process is required" + Fore.RESET)


def slow_print(message):
    print(message)
    time.sleep(1.5)
    print("-" * 50)


if __name__ == "__main__":
    admin_password = AdminPassword()
    slow_print(Fore.BLUE + "Please wait..." + Fore.RESET)

    server_thread = threading.Thread(target=admin_password.start_auth_server)
    server_thread.daemon = True
    server_thread.start()

    slow_print(Fore.BLUE + "Starting server, please wait..." + Fore.RESET)
    password_checker = PasswordChecker(admin_password)

    slow_print(Fore.BLUE + "Checking password, please wait..." + Fore.RESET)
    password_checker.check_password_from_pwned()
    slow_print(Fore.BLUE + "Checking password, please wait..." + Fore.RESET)
    password_checker.check_password_hashed()
    slow_print(Fore.BLUE + "Checking password, please wait..." + Fore.RESET)
    slow_print(Fore.BLUE + "Checking password weakness, please wait..." + Fore.RESET)
    password_checker.check_password_length()
    slow_print(Fore.GREEN + "Password check completed" + Fore.RESET)
    slow_print(Fore.RED + "Mitigation process to follow..." + Fore.RESET)
    password_checker.new_password()

    admin_password.stop_auth_server()
