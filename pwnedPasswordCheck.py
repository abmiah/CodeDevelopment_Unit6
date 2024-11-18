# This is secion of the code pull the top 100,000 passwords from the NCSC website: https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt
# To achieve this, the "requests" library is used get the password list from the NCSC website. "pip install requests" has to be installed to use the requests library
import requests


class pwnedURL:
    """The function will set the URL to pull the top 100,000 passwords from the NCSC website"""
    def __init__(self):
        self.url = "https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt"

    """This function will get the password list from the NCSC website. The function will return the password list 
    if the response status code is 200, otherwise it will return an empty list. The function will split the list 
    for each line for easy reading."""
    def get_password_list(self):
        response = requests.get(self.url, auth = ('user', 'pass'))
        if response.status_code == 200:
            return response.text.splitlines()
        else:
            return []

if __name__ == "__main__":
    url = pwnedURL()
    password_list = url.get_password_list()
    print(password_list)