import time
from colorama import Fore
from adminPassword import AdminPassword
from pwnedPasswordCheck import pwnedURL
from GitHubPasswordCheck import gitHubURL
from hashPassword import PasswordHash
from passwordCount import PasswordCount

class PasswordChecker:
    def __init__(self, admin_password):
        self.admin = admin_password
        self.url = pwnedURL()
        self.url2 = gitHubURL()
        self.hasher = PasswordHash(self.admin)

    def check_password_from_pwned(self):
        password_list = self.url.get_password_list()
        if self.admin.password in password_list:
            print(f"\"{self.admin.password}\" Password is listed in NCSC PwnedPasswordsTop100k.txt")
        else:
            print(f"\"{self.admin.password}\" Password is not listed in NCSC PwnedPasswordsTop100k.txt")

    def check_password_from_github(self):
        password_list = self.url2.get_password_list()
        if self.admin.password in password_list:
            print(f"\"{self.admin.password}\" Password is listed in GitHub 10-million-password-list-top-10000.txt")
        else:
            print(f"\"{self.admin.password}\" Password is not listed in GitHub 10-million-password-list-top-10000.txt")

    def check_password_hashed(self):
        if self.hasher.is_password_hashed(self.admin.password):
            print(f"The password \"{self.admin.password}\" is hashed")
        # Note: The password is hashed in the PasswordHash class should be added to the mitigation section ⚠
        else:
            print(f"The password \"{self.admin.password}\" is not hashed. \"{self.admin.password}\" as hashed \"{self.hasher.hashed_password}\"")

    def check_password_length(self):
        password_count = PasswordCount(self.admin)
        password_count.print_password_length()
        password_count.print_character_types()


if __name__ == "__main__":
    def slow():
        print(Fore.BLUE + "Checking password, Please wait..." + Fore.RESET)
        time.sleep(1.5)
        print("-" * 50)

    admin_password = AdminPassword()
    password_checker = PasswordChecker(admin_password)
    slow()
    password_checker.check_password_from_pwned()
    slow()
    password_checker.check_password_from_github()
    slow()
    password_checker.check_password_hashed()
    slow()
    password_checker.check_password_length()
    slow()
