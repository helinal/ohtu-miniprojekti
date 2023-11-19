class AppLogic():
    def __init__(self):
        self.citations = []

    def add(self, bibtex_object):
        self.citations.append(bibtex_object)

    def return_all(self):
        return self.citations

    def save(self):
        pass
