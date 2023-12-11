import random


class Bibtex():
    def __init__(self, docutype):
        self.docutype = docutype
        self.citekey = None
        self.bibDict = {
        }

    def __str__(self):
        looped = self.loop_to_string()
        return (
            f"@{self.docutype}{{{self.citekey}"
            f"{looped}"
            f"\n}}"
        )

    def create_citekey(self):
        author = self.bibDict["author"].split(', ')
        try:
            year = self.bibDict["year"]
        except KeyError:
            year = random.randint(1000, 10000)

        self.citekey = str(author[0]) + str(year)

    def loop_to_string(self):
        ret = ""
        for key, value in self.bibDict.items():
            not_year = key != "year"
            if not_year:
                ret += f",\n    {key} = \"{value}\""
            else:
                ret += f",\n    {key} = {value}"
        if ret == "":
            return ","
        self.create_citekey()
        return ret

    def add(self, key, value):
        self.bibDict[key] = value
