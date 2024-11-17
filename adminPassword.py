#This first section of code is the admin password section, it will set the admin password and print it to the console

"""This class section is to set the admin password to be checked"""
class AdminPassword:
    """This section sets the admin password to be checked"""
    def __init__(self):
        self.password = input("Please set an admin password: ")

    """The class will then print the password to the console"""
    def print_password(self):
        print("The admin password is:", self.password)


if __name__ == "__main__":
    """This will run the AdminPassword class"""
    admin = AdminPassword()
    admin.print_password()

