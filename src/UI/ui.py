from rich import print # pylint: disable=redefined-builtin
from services.bibtex import Bibtex
from services.app_logic import AppLogic
from services.file_service import File_Saver
from services.doi_service import Doi_Service
from repositories.bibtex_repository import BibTex_Repository
from database_connection import get_data_base_connection


class UI():
    def __init__(self, io, bib_repo=None):
        self.io = io
        self.bib_repo = bib_repo
        if not bib_repo:
            self.bib_repo = BibTex_Repository(get_data_base_connection())
        self.app = AppLogic(self.bib_repo)
        self.file_saver = File_Saver(self.bib_repo)
        self.invalid_message = "[red]\nInvalid input, please try again.[/red]"
        self.doi_service = Doi_Service()

    def start(self):
        while True:
            print("[bright_blue][b]\nChoose an action[/b][/bright_blue]\n" +
                  "1 to add references \n" +
                  "2 to print references \n" +
                  "3 to save references to file \n" +
                  "4 to add by DOI \n" +
                  "5 to stop")
            option = input()

            if option == "1":
                self.add_reference()

            elif option == "2":
                self.print_all()

            elif option == "3":
                self.save_to_file()

            elif option == "4":
                self.add_by_doi()

            elif option == "5":
                break

            else:
                self.io.write_screen(self.invalid_message)

    def add_reference(self):
        while True:
            print("[bright_blue][b]\nChoose the reference type[/b][/bright_blue]\n" +
                  "1 to add article\n" +
                  "2 to add book\n" +
                  "3 to add inproceedings\n" +
                  "4 to add phdthesis\n" +
                  "5 to go back to main menu")
            option = input()

            if option == "1":
                self.add_article()

            elif option == "2":
                self.add_book()

            elif option == "3":
                self.add_inproceedings()

            elif option == "4":
                self.add_phdthesis()

            elif option == "5":
                return

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

    def add_inproceedings(self):
        mand_attributes = ["author", "title"]
        opt_attributes = ["booktitle", "year", "editor", "volume", "number", "series", "pages",
                          "month", "address", "organization", "publisher", "note", "annote"]
        self.app.add(self.add_loop(mand_attributes,
                     opt_attributes, "inproceedings"))

    def add_phdthesis(self):
        mand_attributes = ["author", "title", "school", "year"]
        opt_attributes = ["type", "address", "month", "note", "annote"]
        self.app.add(self.add_loop(mand_attributes,
                     opt_attributes, "phdthesis"))

    def add_loop(self, mand_attributes, opt_attributes, reftype):
        bibtex = self.create_bibtex_obj(reftype)

        for attribute in mand_attributes:
            if attribute == "year":
                bibtex = self.add_year(bibtex)
            else:
                bibtex = self.add_mandatory(bibtex, attribute)

        for attribute in opt_attributes:
            if attribute == "year":
                bibtex = self.add_year(bibtex)
            else:
                bibtex = self.add_optional(bibtex, attribute)

        return bibtex

    def add_by_doi(self):

        doi = self.io.read_input("Enter DOI:")
        data = self.doi_service.fetch(doi)
        if not data:
            self.io.write_screen("[red]\nInvalid DOI, please try again[/red]")
            return
        entry_type = data.entries[0]["ENTRYTYPE"]
        entry_author = data.entries[0]["author"]
        entry_title = data.entries[0]["title"]
        entry_year = data.entries[0]["year"]

        bibtex = Bibtex(entry_type)
        bibtex.add("author", entry_author)
        bibtex.add("title", entry_title)
        bibtex.add("year", entry_year)
        for entry in data.entries:
            for key, value in entry.items():
                if key in ("ENTRYTYPE", "author", "title", "year"):
                    continue
                bibtex.add(key, value)

        self.app.add(bibtex)
        self.io.write_screen("[green]\nReference added successfully![/green]")

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
                    "[red]\nYear needs to be only numbers, try again.\n[/red]")
                continue

    def add_optional(self, bibtex, attribute):
        value = self.io.read_input(f"{attribute} (optional): ")
        if value:
            bibtex.add(attribute, value)
        return bibtex

    def print_all(self):
        all_refs = self.app.return_all()
        self.io.print_readable_form(all_refs)

    def save_to_file(self):
        self.io.write_screen(self.file_saver.write())
