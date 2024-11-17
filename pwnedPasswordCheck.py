#This is secion of the code pull the top 100,000 passwords from the NCSC website
import requests


class pwnedURL:
    def __init__(self):
        self.url = "https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt"

    def get_password_list(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text.splitlines()
        else:
            return []

if __name__ == "__main__":
    url = pwnedURL()
    password_list = url.get_password_list()
    print(password_list)