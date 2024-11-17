from adminPassword import AdminPassword
from pwnedPasswordCheck import pwnedURL
from GitHubPasswordCheck import gitHubURL

class PasswordChecker:
    def __init__(self):
        self.admin = AdminPassword()
        self.url = pwnedURL()
        self.url2 = gitHubURL()

    def check_password_from_pwned(self):
        password_list = self.url.get_password_list()
        if self.admin.password in password_list:
            print(f"\"{self.admin.password}\" is a weak password and is listed in NCSC PwnedPasswordsTop100k.txt")
        else:
            print(f"\"{self.admin.password}\" Password is not listed in NCSC PwnedPasswordsTop100k.txt")

    def check_password_from_github(self):
        password_list = self.url2.get_password_list()
        if self.admin.password in password_list:
            print(f"\"{self.admin.password}\" is a weak password and is listed in GitHub 10-million-password-list-top-10000.txt")
        else:
            print(f"\"{self.admin.password}\" Password is not listed in GitHub 10-million-password-list-top-10000.txt")

if __name__ == "__main__":
    password_checker = PasswordChecker()
    password_checker.check_password_from_pwned()
    password_checker.check_password_from_github()