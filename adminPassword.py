# This code defines the admin password class and prints the password to the console.
# The class imports the "socket" and "requests" to create a server that listens for incoming connections.
import socket
import requests


class AdminPassword:
    """ Section sets the admin password and print the password to the console """

    def __init__(self):
        self.password = input("Please set an admin password: ")
        print(f"The admin password for the IoT Hub is: {self.password}")
        self.weak_passwords = self.load_weak_passwords()
        self.running = True

    """ The "load_weak_passwords" method uses the "requests" library to download and store the top 100,000 
    passwords from the NCSC. """

    @staticmethod
    def load_weak_passwords():
        url = 'https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt'
        response = requests.get(url)
        if response.status_code == 200:
            return set(response.text.splitlines())
        else:
            print("Failed to load weak passwords list. Using a default list.")
            return {'password', '123456', 'admin'}

    """ Checks if the password is weak by comparing it to the weak password list from the NCSC website. """

    def is_weak_password(self, password):
        return password in self.weak_passwords

    """ This function starts an authentication server on localhost at a specified port, listening for client connections. 
    It checks the submitted password against the admin password, sending a success message if they match, or a failure 
    message if they do not. """

    def start_auth_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 12345))
        server_socket.listen(1)
        print("Authentication server started on localhost:12345")

        """ The "try" and "except" block below listens for incoming client connections and reads password attempts, 
        helping to manage exceptions in the "start_auth_server" method. """
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

    """ This stops the authentication server by setting the "running" attribute to "False", stopping the 
    connections and exits the "start_auth_server" loop. """

    def stop_auth_server(self):
        self.running = False


if __name__ == "__main__":
    admin = AdminPassword()
    admin.start_auth_server()
