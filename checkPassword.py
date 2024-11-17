from adminPassword import AdminPassword
from pwnedPasswordCheck import pwnedURL

class PasswordChecker:
    def __init__(self):
        self.admin = AdminPassword()
        self.url = pwnedURL()

    def check_password(self):
        password_list = self.url.get_password_list()
        if self.admin.password in password_list:
            print(f"{self.admin.password} Password is weak and is listed in NCSC PwnedPasswordsTop100k.txt")
        else:
            print("Password is strong")

if __name__ == "__main__":
    password_checker = PasswordChecker()
    password_checker.check_password()