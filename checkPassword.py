from adminPassword import AdminPassword
from pwnedPasswordCheck import pwnedURL
from GitHubPasswordCheck import gitHubURL
from hashPassword import PasswordHash

class PasswordChecker:
    def __init__(self, admin_password):
        self.admin = admin_password
        self.url = pwnedURL()
        self.url2 = gitHubURL()
        self.hasher = PasswordHash(self.admin)

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

    def check_password_hashed(self):
        if self.hasher.is_password_hashed(self.admin.password):
            print(f"The password \"{self.admin.password}\" is hashed")
        else:
            print(f"The password \"{self.admin.password}\" is not hashed. \"{self.admin.password}\" as hashed \"{self.hasher.hashed_password}\"")

if __name__ == "__main__":
    admin_password = AdminPassword()
    password_checker = PasswordChecker(admin_password)
    password_checker.check_password_from_pwned()
    password_checker.check_password_from_github()
    password_checker.check_password_hashed()