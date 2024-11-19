# This code defines the admin password class and prints the password to the console for testing.

"""This part of the class sets the admin password to verify the program."""


class AdminPassword:
    """Section sets the admin password and print the password to the console"""

    def __init__(self):
        self.password = input("Please set an admin password: ")
        print(f"The admin password for the IoT Hub is: {self.password}")


if __name__ == "__main__":
    admin = AdminPassword()
