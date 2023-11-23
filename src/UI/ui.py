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
                self.add_article()

            elif option == "2":
                self.print_all()

            elif option == "3":
                break

            else:
                self.io.write_screen("invalid input, try again")

    def add_article(self):
        code = self.io.read_input("Citekey: ")
        bibtex = Bibtex("article", code)

        author = self.io.read_input("Author: ")
        bibtex.add("author", author)

        title = self.io.read_input("Title: ")
        bibtex.add("title", title)

        journal = self.io.read_input("Journal: ")
        bibtex.add("journal", journal)

        try:
            year = int(input("Year: "))
            bibtex.add("year", year)

        except ValueError:
            self.io.write_screen("year needs to be only numbers, try again")
            return

        self.app.add(bibtex)

    def add_book(self):
        pass

    def add_inproceeding(self):
        pass

    def print_all(self):
        all_refs = self.app.return_all()
        for x in all_refs:
            self.io.write_screen(x)
