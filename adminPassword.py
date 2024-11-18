# This first section of code is the admin password class, it will set the admin password and print it to the console to be tested

"""This class section sets the admin password to be checked by the rest of the program"""
class AdminPassword:
    """Section sets the admin password"""
    def __init__(self):
        self.password = input("Please set an admin password: ")

    """The class will print the password to the console"""
    def print_password(self):
        print("The admin password is:", self.password)


if __name__ == "__main__":
    """This will run the AdminPassword class"""
    admin = AdminPassword()
    admin.print_password()

