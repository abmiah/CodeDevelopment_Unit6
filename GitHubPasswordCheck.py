# This section of the code pulls the top 10 million passwords from GitHub.
# https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top
# -1000000.txt Use the "requests" library to fetch the password list from GitHub. Install it with "pip install requests.

import requests

"""This part of the code will retrieve data from the GitHub website."""


class GitHubURL:
    """This function sets the URL to retrieve the top 10 million passwords from GitHub's raw file."""

    def __init__(self):
        self.url = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt"

    """This function fetches the data from the NCSC website. It returns the list if the status code is 200; 
    otherwise, it returns an empty list, formatted with each password on a separate line for clarity."""

    def get_password_list(self):
        response = requests.get(self.url, auth=('user', 'pass'))
        if response.status_code == 200:
            return response.text.splitlines()
        else:
            return []


if __name__ == "__main__":
    url = GitHubURL()
    password_list = url.get_password_list()
    print(password_list)
