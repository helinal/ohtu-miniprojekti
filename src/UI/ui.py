from services.bibtex import Bibtex
from services.app_logic import AppLogic


class UI():
    def __init__(self, io):
        self.io = io
        self.app = AppLogic()

    def start(self):
        while True:
            try:
                option = self.io.read_input(
                    "Choose 1 to add article references or choose 2 to print references or 3 to stop: ")
            except ValueError:
                self.io.write_screen("invalid input, try again")
                continue

            if option == "1":
                self.add_reference()

            elif option == "2":
                self.print_all()

            elif option == "3":
                break

            else:
                self.io.write_screen("invalid input, try again")

    def add_reference(self):
        while True:
            try:
                option = self.io.read_input(
                    "Choose reference type (article or book):")
            except ValueError:
                self.io.write_screen("invalid input, try again")
                continue

            if option.lower() == "article":
                self.add_article()
                break

            elif option == "book":
                self.add_book()
                break

            else:
                self.io.write_screen("invalid input, try again")

    def add_article(self):
        attributes = ["author", "title", "journal", "year", "volume", "number", "pages", "month", "note"]
        self.app.add(self.add_loop(attributes, "article"))

    
    def add_book(self):
        attributes = ["author", "editor", "title", "publisher", "year", "volume", "number", "pages", "month", "note"]
        self.app.add(self.add_loop(attributes, "book"))

    def add_inproceeding(self):
        pass

    def add_loop(self, attributes, reftype):
        code = self.io.read_input("Citekey: ")
        bibtex = Bibtex(reftype, code)

        for attribute in attributes:
            if attribute == "year":
                while True:
                    try:
                        year = int(input("Year: "))
                        bibtex.add("year", year)
                        break

                    except ValueError:
                        self.io.write_screen("year needs to be only numbers, try again")
                        continue
            else:
                value = self.io.read_input(f"{attribute}: ")  # Reading input for each attribute
                bibtex.add(attribute, value)

        return bibtex    

    def print_all(self):
        all_refs = self.app.return_all()
        for x in all_refs:
            self.io.write_screen(x)
