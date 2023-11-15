class AppLogic():
    def __init__(self):
        self.citations = []

    def add(self, object):
        self.citations.append(object)

    def return_all(self):
        return self.citations

    def save(self):
        pass