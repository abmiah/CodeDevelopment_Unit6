#This is secion of the code pull the top 10 million passwords from the GitHub
import requests

"""This section of the code will pull the top 10 million passwords from the GitHub website"""
class gitHubURL:
    """This section sets the URL to pull the top 10 million passwords from the GitHub website"""
    """The url grabs the raw file from the GitHub repository"""
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt"


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