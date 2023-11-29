from services.bibtex import Bibtex
from services.app_logic import AppLogic
from repositories.bibtex_repository import BibTex_Repository
from database_connection import get_data_base_connection
from services.file_service import File_Saver


class UI():
    def __init__(self, io):
        self.io = io
        self.bib_repo = BibTex_Repository(get_data_base_connection())
        self.app = AppLogic(self.bib_repo)
        self.file_saver = File_Saver(self.bib_repo)
        self.invalid_message = "Invalid input, try again."

    def start(self):
        while True:

            option = self.io.read_input(
                "Choose an action: \n" +
                "1 to add references \n" +
                "2 to print references \n" +
                "3 to save references to file \n" +
                "4 to stop \n")

            if option == "1":
                self.add_reference()

            elif option == "2":
                self.print_all()

            elif option == "3":
                self.save_file()

            elif option == "4":
                break

            else:
                self.io.write_screen(self.invalid_message)

    def add_reference(self):
        while True:
            option = self.io.read_input(
                "Choose reference type: \n" +
                "1 to add article\n" +
                "2 to add book\n" +
                "3 to go back to main menu \n")

            if option == "1":
                self.add_article()
                break

            if option == "2":
                self.add_book()
                break

            if option == "3":
                return

            self.io.write_screen(self.invalid_message)

    def add_article(self):
        mand_attributes = ["author", "title", "journal", "year"]
        opt_attributes = ["volume", "number", "pages", "month", "note"]
        self.app.add(self.add_loop(mand_attributes, opt_attributes, "article"))

    def add_book(self):
        mand_attributes = ["author", "editor", "title", "publisher", "year"]
        opt_attributes = ["volume", "number", "pages", "month", "note"]
        self.app.add(self.add_loop(mand_attributes, opt_attributes, "book"))

    def add_loop(self, mand_attributes, opt_attributes, reftype):
        bibtex = self.create_bibtex_obj(reftype)

        for attribute in mand_attributes:
            if attribute == "year":
                bibtex = self.add_year(bibtex)
            else:
                bibtex = self.add_mandatory(bibtex, attribute)

        for attribute in opt_attributes:
            bibtex = self.add_optional(bibtex, attribute)

        return bibtex

    def create_bibtex_obj(self, reftype):
            bibtex = Bibtex(reftype)
            return bibtex


    def add_mandatory(self, bibtex, attribute):
        while True:
            value = self.io.read_input(f"{attribute} (mandatory): ")
            if value.strip():
                bibtex.add(attribute, value)
                return bibtex

            self.io.write_screen(self.invalid_message)

    def add_year(self, bibtex):
        while True:
            try:
                year = int(self.io.read_input("year (mandatory): "))
                bibtex.add("year", year)
                return bibtex

            except ValueError:
                self.io.write_screen(
                    "Year needs to be only numbers, try again.")
                continue

    def add_optional(self, bibtex, attribute):
        value = self.io.read_input(f"{attribute} (optional): ")
        if value:
            bibtex.add(attribute, value)
        return bibtex

    def print_all(self):
        all_refs = self.app.return_all()
        for x in all_refs:
            self.io.print_readable_form(x)
    
    def save_file(self):
        self.file_saver.write()

