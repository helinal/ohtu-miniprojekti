class AppLogic():
    def __init__(self, bib_repo):
        self.bib_repo = bib_repo
        self.citations = self.initialize_citations()

    def initialize_citations(self):
        return self.bib_repo.fetch_all()

    def add(self, bibtex_object):
        bibtex_object.create_citekey()
        self.bib_repo.save(bibtex_object)
        self.citations = self.initialize_citations()

    def return_all(self):
        return self.citations
