import time
from colorama import Fore
from adminPassword import AdminPassword
from pwnedPasswordCheck import PwnedURL
from GitHubPasswordCheck import GitHubURL
from hashPassword import PasswordHash
from passwordCount import PasswordCount
from newPassword import NewPassword


class PasswordChecker:
    def __init__(self, admin_password):
        self.admin = admin_password
        self.url = PwnedURL()
        self.url2 = GitHubURL()
        self.hasher = PasswordHash(self.admin)
        self.new_random_password = NewPassword()

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
        password_count.print_password_strength()

    def new_password(self):
        print(f"{self.new_random_password.password.print_password}")


def slow_print(message):
    print(message)
    time.sleep(0.5)
    print("-" * 50)


if __name__ == "__main__":
    admin_password = AdminPassword()
    password_checker = PasswordChecker(admin_password)

    slow_print(Fore.BLUE + "Checking password, Please wait..." + Fore.RESET)
    password_checker.check_password_from_pwned()
    slow_print(Fore.BLUE + "Checking password, Please wait..." + Fore.RESET)
    password_checker.check_password_from_github()
    slow_print(Fore.BLUE + "Checking password, Please wait..." + Fore.RESET)
    password_checker.check_password_hashed()
    slow_print(Fore.BLUE + "Checking password, Please wait..." + Fore.RESET)
    password_checker.check_password_length()
    slow_print(Fore.GREEN + "Password check completed" + Fore.RESET)
    slow_print(Fore.RED + "Mitigation process to follow..." + Fore.RESET)
    password_checker.new_password()

