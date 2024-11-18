# This is secion of the code pull the top 10 million passwords from the GitHub: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
# The "requests" library is used get the password list from the GitHub website. "pip install requests" has to be installed to use the requests library
import requests

"""This section of the code will pull the top 10 million passwords from the GitHub website"""
class gitHubURL:
    """This function sets the URL to pull the top 10 million passwords from the GitHub website.
    The url grabs the raw file from the GitHub repository"""
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt"

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
    url = gitHubURL()
    password_list = url.get_password_list()
    print(password_list)