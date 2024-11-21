# This code defines the admin password class and prints the password to the console for testing.
# The class imports the socket and requests libraries to create a server that listens for incoming connections.
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

    """The "load_weak_passwords" method retrieves the top 100,000 passwords from the NCSC website and stores them in 
    a set. It utilizes the "requests" library to download the password list from the NCSC website."""
    @staticmethod
    def load_weak_passwords():
        url = 'https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt'
        response = requests.get(url)
        if response.status_code == 200:
            return set(response.text.splitlines())
        else:
            print("Failed to load weak passwords list. Using a default list.")
            return {'password', '123456', 'admin'}

    """The function below checks if a password is weak by comparing it to the weak password list from the NCSC website."""
    def is_weak_password(self, password):
        return password in self.weak_passwords

    """This function initiates the authentication server on localhost at the specified port number. It listens 
    for incoming connections from clients. When a connection is established, the server reads the password attempt 
    submitted by the client. If this password attempt matches the admin password, the server responds with a message 
    indicating that authentication was successful. Conversely, if the password attempt does not match the admin 
    password, the server sends a message indicating that authentication failed. After processing the password attempt, 
    the server closes the connection with the client."""
    def start_auth_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 12345))
        server_socket.listen(1)
        print("Authentication server started on localhost:12345")

        """The "try" and "except" block below listens for incoming connections from clients and reads the password 
        attempts. This was added to the "start_auth_server" method to manage exceptions that may occur during 
        the server's operation."""
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

    """The function below stops the authentication server by setting the "running" attribute to False.This causes
    the server to stop listening for incoming connections and exit the loop in the "start_auth_server" method."""
    def stop_auth_server(self):
        self.running = False


if __name__ == "__main__":
    admin = AdminPassword()
    admin.start_auth_server()
