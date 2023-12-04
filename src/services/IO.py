from rich import print # pylint: disable=redefined-builtin


class KonsoliIO():
    def read_input(self, text):
        return input(text)

    def write_screen(self, text):
        print(text)

    def print_readable_form(self, text):
        if not text:
            print("[red]\nYou do not have any references to print![/red]")

        for i in text:
            doc_type = i.docutype
            citekey = i.citekey

            print(
                f"[medium_purple1][b]\nType: {doc_type}, citekey: {citekey}[/b][/medium_purple1]")
            for key, value in i.bibDict.items():
                print(f"{key}: {value}")
