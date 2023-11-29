import requests

class Doi_Service:
    def __init__(self):
        self.doi_url = 'https://www.doi.org/'
        self.headers = {"accept": "application/x-bibtex"}

    def fetch(self, doi):
        url = f"{self.doi_url}/{doi}"
        