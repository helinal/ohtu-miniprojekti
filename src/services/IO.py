from bibtex import Bibtex
from app_logic import AppLogic

class KonsoliIO:
    def __init__(self):
        self.app = AppLogic()

    def add_article(self):
        code = input("Citekey: ")
        bibtex = Bibtex("article", code)

        author = input("Author: ")
        bibtex.add("author", author)

        title = input("Title: ")
        bibtex.add("title", title)

        journal = input("Journal: ")
        bibtex.add("journal", journal)

        try:
            year = int(input("Year: "))
            bibtex.add("year", year)

        except ValueError:
            print("year needs to be only numbers, try again")
            return

        self.app.add(bibtex)

    def add_book(self):
        pass

    def add_inproceeding(self):
        pass

    def print(self):
        all_refs = self.app.return_all()
        for x in all_refs:
            print(x)


class UI:
    def __init__(self, io):
        self.io = io

    def start(self):
        while True:
            try:
                option = int(input("Choose 1 to add article references or choose 2 to print references or 3 to stop: "))
            except ValueError:
                print("invalid input, try again")
                continue

            if option == 1:
                self.io.add_article()

            elif option == 2:
                self.io.print()

            elif option == 3:
                break

            else:
                print("invalid input, try again")


def main():
    io = KonsoliIO()
    ui = UI(io)

    ui.start()

main()
