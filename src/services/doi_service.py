import requests
import bibtexparser


class Doi_Service:
    def __init__(self):
        self.doi_url = 'https://dx.doi.org/'
        self.headers = {"accept": "application/x-bibtex"}

    def fetch(self, doi):
        url = f"{self.doi_url}/{doi}"
        try:
            req = requests.get(url, headers=self.headers, timeout=10)

            data = None
            if req.status_code == 200:
                data = bibtexparser.loads(req.text)

            return data
        except requests.Timeout:
            return None
