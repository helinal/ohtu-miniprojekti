class AppLogic():
    def __init__(self, bib_repo):
        self.bib_repo = bib_repo
        self.citations = self.initialize_citations()

    def initialize_citations(self):
        return self.bib_repo.fetch_all()

    def add_reference(self, bibtex_object, tag='NULL'):
        bibtex_object.create_citekey()
        self.bib_repo.save(bibtex_object, tag)
        self.citations = self.initialize_citations()

    def delete_reference(self, citekey):
        status = self.bib_repo.delete_object(citekey)
        self.citations = self.initialize_citations()
        return status

    def find_reference(self, tag):
        return self.bib_repo.find_reference(tag)

    def return_all(self):
        return self.citations
