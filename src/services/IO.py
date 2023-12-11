from rich.console import Console


class KonsoliIO():
    def __init__(self):
        self.console = Console()

    def read_input(self, text):
        return input(text)

    def write_screen(self, text):
        self.console.print(text)

    def print_readable_form(self, references):
        if not references:
            self.console.print(
                "\n[bold red]You do not have any references to print![bold red]")
            return

        for ref in references:
            doc_type = ref.docutype
            citekey = ref.citekey

            self.console.print(
                f"\n[bold bright_blue]Type: {doc_type}, Citekey: {citekey}[/bold bright_blue]")
            for key, value in ref.bibDict.items():
                self.console.print(f"{key:10} {value}")
