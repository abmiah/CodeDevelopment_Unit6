# This section of the code will count the length of the password and check the character types
from adminPassword import AdminPassword

class PasswordCount:
    def __init__(self, admin_password):
        self.admin = admin_password
        self.count = self.count_password_length(self.admin.password)
        self.character_types = self.check_character_types(self.admin.password)

    def count_password_length(self, password):
        return len(password)

    def print_password_length(self):
        if self.count < 8:
            print(f"The length of the password is for \"{self.admin.password}\": is {self.count} characters long")
            print(f"The password should be at least 8 characters long")
        else:
            print(f"The length of the password for \"{self.admin.password}\" is {self.count} characters long")

    def check_character_types(self, password):
        types = {
            "Uppercase": sum(1 for char in password if char.isupper()),
            "Lowercase": sum(1 for char in password if char.islower()),
            "Numeric": sum(1 for char in password if char.isdigit()),
            "Special": sum(1 for char in password if not char.isalnum()),
        }
        return types

    def print_character_types(self):
        print(f"Password \"{self.admin.password}\" contains:")
        for key, value in self.character_types.items():
            # print(f"{key}: {'Yes' if value else 'No'}")
            print(f"{key}: {'Yes' if value else 'No'} = {value} characters")


if __name__ == "__main__":
    admin = AdminPassword()
    password_count = PasswordCount(admin)
    password_count.print_password_length()
    password_count.print_character_types()
