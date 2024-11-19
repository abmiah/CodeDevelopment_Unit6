# This section of the code will count the length of the password and check the character types
# The code will use the AdminPassword class from adminPassword.py file to set the password and check the password length and character types import types

from adminPassword import AdminPassword

"""This class will count the length of the password and check the character types"""
class PasswordCount:
    def __init__(self, admin_password):
        self.admin = admin_password
        self.count = self.count_password_length(self.admin.password)
        self.character_types = self.check_character_types(self.admin.password)

    """The function below will count the length of the password"""
    def count_password_length(self, password):
        return len(password)

    """The function below will print the length of the password to the console. The function uses the "if" and "else" 
    statement to check if the password is less than 8 characters long"""
    def print_password_length(self):
        if self.count < 8:
            print(f"The length of the password is for \"{self.admin.password}\": is {self.count} characters long")
            print(f"The password should be at least 8 characters long")
        else:
            print(f"The length of the password for \"{self.admin.password}\" is {self.count} characters long")

    """The function method below will check the character types of the password. The method uses a dictionary to 
    store the values of the character types. The function uses the "isupper", "islower", "isdigit" and "isalnum" 
    functions to check the character types."""
    def check_character_types(self, password):
        types = {
            "Uppercase": sum(1 for char in password if char.isupper()),
            "Lowercase": sum(1 for char in password if char.islower()),
            "Numeric": sum(1 for char in password if char.isdigit()),
            "Special": sum(1 for char in password if not char.isalnum()),
        }
        return types

    """The final part of the function will print the character types to the console. The "for" loop will iterate through 
    the dictionary and print the character types to the console"""
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
