import requests
import bibtexparser

class Doi_Service:
    def __init__(self):
        self.doi_url = 'https://dx.doi.org/'
        self.headers = {"accept": "application/x-bibtex"}

    def fetch(self, doi):
        url = f"{self.doi_url}/{doi}"
        req = requests.get(url, headers=self.headers)

        data = None
        if req.status_code == 200:
            data = req.text

        return data
