from services.bibtex import Bibtex
from services.app_logic import AppLogic
from repositories.bibtex_repository import BibTex_Repository
from database_connection import get_data_base_connection


class UI():
    def __init__(self, io):
        self.io = io
        self.app = AppLogic(BibTex_Repository(get_data_base_connection()))
        self.invalid_message = "Invalid input, try again."

    def start(self):
        while True:
            try:
                option = self.io.read_input(
                    "Choose 1 to add article references or choose 2 to print references or 3 to stop: ")
            except ValueError:
                self.io.write_screen(self.invalid_message)
                continue

            if option == "1":
                self.add_reference()

            elif option == "2":
                self.print_all()

            elif option == "3":
                break

            else:
                self.io.write_screen(self.invalid_message)

    def add_reference(self):
        while True:
            try:
                option = self.io.read_input(
                    "Choose reference type (article or book):")
            except ValueError:
                self.io.write_screen(self.invalid_message)
                continue

            if option.lower() == "article":
                self.add_article()
                break

            elif option == "book":
                self.add_book()
                break

            else:
                self.io.write_screen(self.invalid_message)

    def add_article(self):
        mand_attributes = ["author", "title", "journal", "year"]
        opt_attributes = ["volume", "number", "pages", "month", "note"]
        self.app.add(self.add_loop(mand_attributes, opt_attributes, "article"))

    
    def add_book(self):
        mand_attributes = ["author", "editor", "title", "publisher", "year"]
        opt_attributes = ["volume", "number", "pages", "month", "note"]
        self.app.add(self.add_loop(mand_attributes, opt_attributes, "book"))

    def add_inproceeding(self):
        pass

    def add_loop(self, mand_attributes, opt_attributes, reftype):
        bibtex = self.add_citekey(reftype)

        for attribute in mand_attributes:
            if attribute == "year":
                bibtex = self.add_year(bibtex)
            else:
                bibtex = self.add_mandatory(bibtex, attribute)

        for attribute in opt_attributes:
            bibtex = self.add_optional(bibtex, attribute)

        return bibtex    
    
    def add_citekey(self, reftype):
        while True:
            code = self.io.read_input("Citekey: ")
            if code.strip():
                bibtex = Bibtex(reftype, code)
                return bibtex
            else:
                print(self.invalid_message)

    def add_mandatory(self, bibtex, attribute):
        while True:
            value = self.io.read_input(f"{attribute} (mandatory): ")
            if value.strip():
                bibtex.add(attribute, value)
                return bibtex
            else:
                print(self.invalid_message)

    def add_year(self, bibtex):
        while True:
            try:
                year = int(input("year (mandatory): "))
                bibtex.add("year", year)
                return bibtex

            except ValueError:
                self.io.write_screen("Year needs to be only numbers, try again")
                continue

    def add_optional(self, bibtex, attribute):
        value = self.io.read_input(f"{attribute} (optional): ")
        if value:
            bibtex.add(attribute, value)
        return bibtex

    def print_all(self):
        all_refs = self.app.return_all()
        for x in all_refs:
            self.io.write_screen(x)