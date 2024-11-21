# This part of the code checks how long the password is and identifies the types of characters used.
# The code uses the "AdminPassword" class from "adminPassword.py" to set and verify the password length and character types.

from adminPassword import AdminPassword

""" This class will measure the length of a password and check what types of characters it contains. """


class PasswordCount:
    def __init__(self, admin_password):
        self.admin = admin_password
        self.count = self.count_password_length(self.admin.password)
        self.character_types = self.check_character_types(self.admin.password)
        self.score = self.evaluate_password_strength()

    """ The function below measures how long the password is. """

    @staticmethod
    def count_password_length(password):
        return len(password)

    """ The function below prints the length of a password and checks if it is shorter than 8 characters using 
    "if" statements. """

    def print_password_length(self):
        print(f"The password length \"{self.admin.password}\": is {self.count} characters long")
        if self.count <= 8:
            print("The password should be at least 8 characters long")
            print("Your password must combine uppercase, lowercase, numbers, and special characters.")

    """ The method below checks the character types of a password, using a dictionary to store their values. """

    @staticmethod
    def check_character_types(password):
        return {
            "Uppercase": sum(1 for char in password if char.isupper()),
            "Lowercase": sum(1 for char in password if char.islower()),
            "Numeric": sum(1 for char in password if char.isdigit()),
            "Special": sum(1 for char in password if not char.isalnum()),
        }
        # return types

    """ The function ends by printing character types to the console using a "for" loop that goes through the dictionary. """

    def print_character_types(self):
        print(f"Password \"{self.admin.password}\" contains:")
        for key, value in self.character_types.items():
            # print(f"{key}: {'Yes' if value else 'No'}")
            print(f"{key}: {'Yes' if value else 'No'} = {value} characters")

    """ The function checks how strong a password is by looking at its length and the types of characters it uses. """

    def evaluate_password_strength(self):
        score = sum([
            self.count >= 8,
            self.character_types["Uppercase"] > 1,
            self.character_types["Lowercase"] > 1,
            self.character_types["Numeric"] > 1,
            self.character_types["Special"] > 1
        ])
        return "Weak" if score <= 2 else "Moderate" if score <= 4 else "Strong"

    def print_password_strength(self):
        print(f"Password \"{self.admin.password}\" has a strength rating of: {self.score}")

    def is_password_weak(self):
        return len(self.admin.password) < 8 or self.score in {"Weak", "Moderate"}


if __name__ == "__main__":
    admin = AdminPassword()
    password_count = PasswordCount(admin)
    password_count.print_password_length()
    password_count.print_character_types()
    password_count.print_password_strength()
