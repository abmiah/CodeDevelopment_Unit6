# This code defines the admin password class and prints the password to the console for testing.
import socket
import requests

"""This part of the class sets the admin password to verify the program."""


class AdminPassword:
    """Section sets the admin password and print the password to the console"""

    def __init__(self):
        self.password = input("Please set an admin password: ")
        print(f"The admin password for the IoT Hub is: {self.password}")
        self.weak_passwords = self.load_weak_passwords()
        self.running = True

    def load_weak_passwords(self):
        url = 'https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt'
        response = requests.get(url)
        if response.status_code == 200:
            return set(response.text.splitlines())
        else:
            print("Failed to load weak passwords list. Using a default list.")
            return set(['password', '123456', 'admin'])

    def is_weak_password(self, password):
        return password in self.weak_passwords

    def start_auth_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 12345))
        server_socket.listen(1)
        print("Authentication server started on localhost:12345")

        try:
            while self.running:
                client_socket, address = server_socket.accept()
                print(f"Connection from {address}")

                password_attempt = client_socket.recv(1024).decode().strip()

                if password_attempt == self.password:
                    if self.is_weak_password(password_attempt):
                        response = "Authentication successful, but password is weak. Please change it."
                    else:
                        response = "Authentication successful."
                else:
                    response = "Authentication failed."

                client_socket.send(response.encode())
                client_socket.close()
        except KeyboardInterrupt:
            print("\nThe server is shutting down...")
        finally:
            server_socket.close()

    def stop_auth_server(self):
        self.running = False


if __name__ == "__main__":
    admin = AdminPassword()
    admin.start_auth_server()
