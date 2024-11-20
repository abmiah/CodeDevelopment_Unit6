# This part of the code gets the top 100,000 passwords from the NCSC website.
# https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt Use the "requests" library to download
# the password list from the NCSC website. Install it with "pip install requests.import requests

import requests


class PwnedURL:
    """The function will set the URL from the NCSC website."""

    def __init__(self):
        self.url = "https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt"

    """The NewPassword class generates an 18-character password using letters, digits, and punctuation. It includes a 
    "random_password" method to create the password and a "print_password" method to display the password with its 
    hashed value."""

    def get_password_list(self):
        response = requests.get(self.url, auth=('user', 'pass'))
        if response.status_code == 200:
            return response.text.splitlines()
        else:
            return []


if __name__ == "__main__":
    url = PwnedURL()
    password_list = url.get_password_list()
    print(password_list)
