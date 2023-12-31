from rich.console import Console
from services.bibtex import Bibtex
from services.app_logic import AppLogic
from services.file_service import FileService
from services.doi_service import DoiService
from repositories.bibtex_repository import BibTexRepository
from database_connection import get_database_connection


class UI():
    def __init__(self, io, bib_repo=None):
        self.io = io
        self.bib_repo = bib_repo
        if not bib_repo:
            self.bib_repo = BibTexRepository(get_database_connection())
        self.app = AppLogic(self.bib_repo)
        self.file_saver = FileService(self.bib_repo)
        self.invalid_message = "[bold red]\nInvalid input, please try again.[/bold red]"
        self.doi_service = DoiService()
        self.console = Console()

    def start(self):
        while True:
            self.console.print(
                "\n[bold cyan1]Choose an action:[/bold cyan1]\n" +
                "1 to [bright_blue]add references[/bright_blue]\n" +
                "2 to [bright_blue]print references[/bright_blue]\n" +
                "3 to [bright_blue]save references to file[/bright_blue]\n" +
                "4 to [bright_blue]add by DOI[/bright_blue]\n" +
                "5 to [bright_blue]delete a reference[/bright_blue]\n" +
                "6 to [bright_blue]search saved references with tag[/bright_blue]\n" +
                "7 to [bright_blue]stop[/bright_blue]\n"
            )

            option = self.io.read_input(">>> ")

            if option == "1":
                self.add_reference()

            elif option == "2":
                self.print_all()

            elif option == "3":
                self.save_to_file()

            elif option == "4":
                self.add_by_doi()

            elif option == "5":
                self.delete_reference()

            elif option == "6":
                self.find_reference()

            elif option == "7":
                break

            else:
                self.io.write_screen(self.invalid_message)

    def delete_reference(self):
        self.io.write_screen(
            "\nEnter the citekey of the reference you want to delete:\n ")
        citekey = self.io.read_input('>>> ')
        status = self.app.delete_reference(citekey)
        if status is True:
            self.io.write_screen("\n[bold green]Deleted[/bold green]")
        if status is False:
            self.io.write_screen("\n[bold red]Delete failed[/bold red]")

    def add_reference(self):
        while True:
            self.console.print(
                "\n[bold cyan2]Choose reference type:[/bold cyan2]\n" +
                "[cyan]1[/cyan] to [bright_blue]add article[/bright_blue]\n" +
                "[cyan]2[/cyan] to [bright_blue]add book[/bright_blue]\n" +
                "[cyan]3[/cyan] to [bright_blue]add inproceedings[/bright_blue]\n" +
                "[cyan]4[/cyan] to [bright_blue]add phdthesis[/bright_blue]\n" +
                "[cyan]5[/cyan] to [bright_blue]go back to main menu[/bright_blue]\n"
            )

            option = self.io.read_input(">>> ")

            if option == "1":
                self.add_article()
                break

            if option == "2":
                self.add_book()
                break

            if option == "3":
                self.add_inproceedings()
                break

            if option == "4":
                self.add_phdthesis()
                break

            if option == "5":
                return

            self.io.write_screen(self.invalid_message)

    def add_article(self):
        mand_attributes = ["author", "title", "journal", "year"]
        opt_attributes = ["volume", "number", "pages", "month", "note"]
        self.app.add_reference(self.add_loop(
            mand_attributes, opt_attributes, "article"), self.add_tags())
        self.io.write_screen(
            "\n[bold green]Reference added successfully![/bold green]")

    def add_book(self):
        mand_attributes = ["author", "editor", "title", "publisher", "year"]
        opt_attributes = ["volume", "number", "pages", "month", "note"]
        self.app.add_reference(self.add_loop(
            mand_attributes, opt_attributes, "book"), self.add_tags())
        self.io.write_screen(
            "\n[bold green]Reference added successfully![/bold green]")

    def add_inproceedings(self):
        mand_attributes = ["author", "title"]
        opt_attributes = ["booktitle", "year", "editor", "volume", "number", "series", "pages",
                          "month", "address", "organization", "publisher", "note", "annote"]
        self.app.add_reference(self.add_loop(mand_attributes,
                                             opt_attributes, "inproceedings"), self.add_tags())
        self.io.write_screen(
            "\n[bold green]Reference added successfully![/bold green]")

    def add_phdthesis(self):
        mand_attributes = ["author", "title", "school", "year"]
        opt_attributes = ["type", "address", "month", "note", "annote"]
        self.app.add_reference(self.add_loop(mand_attributes,
                                             opt_attributes, "phdthesis"), self.add_tags())
        self.io.write_screen(
            "\n[bold green]Reference added successfully![/bold green]")

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

        doi = self.io.read_input("\nEnter DOI:")
        data = self.doi_service.fetch(doi)
        if not data or not data.entries:
            self.io.write_screen(
                "\n[bold red]Invalid DOI, please try again[/bold red]")
            return
        self.create_from_doi_object(data.entries)
        self.io.write_screen(
            "\n[bold green]Reference added successfully![bold green]")

    def create_from_doi_object(self, data):
        entry_type = data[0]["ENTRYTYPE"]
        entry_author = data[0]["author"]
        entry_title = data[0]["title"]
        entry_year = data[0]["year"]

        bibtex = Bibtex(entry_type)
        bibtex.add("author", entry_author)
        bibtex.add("title", entry_title)
        bibtex.add("year", entry_year)
        for entry in data:
            for key, value in entry.items():
                if key in ("ENTRYTYPE", "author", "title", "year"):
                    continue
                bibtex.add(key, value)

        tag = self.add_tags()
        self.app.add_reference(bibtex, tag)

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
                    "\n[bold red]Year needs to be only numbers, try again.[/bold red]\n")
                continue

    def add_optional(self, bibtex, attribute):
        value = self.io.read_input(f"{attribute} (optional): ")
        if value:
            bibtex.add(attribute, value)
        return bibtex

    def add_tags(self):
        tagstring = self.io.read_input(
            "tags (optional, separated by a comma): ")
        if tagstring == '':
            return 'DEFAULT'
        return tagstring

    def print_all(self):
        all_refs = self.app.return_all()
        self.io.print_readable_form(all_refs)

    def save_to_file(self):
        self.io.write_screen(self.file_saver.write())

    def find_reference(self):
        tag = self.io.read_input(
            "\nEnter the tag of the reference you want to find: ")
        result = self.app.find_reference(tag)
        if result:
            self.io.print_readable_form(result)
        else:
            self.io.write_screen("\n[bold red]Tag not found[/bold red]")
