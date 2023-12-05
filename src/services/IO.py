class KonsoliIO():
    def read_input(self, text):
        return input(text)

    def write_screen(self, text):
        print(text)

    def print_readable_form(self, references):
        if not references:
            print("\nYou do not have any references to print!\n")

        for ref in references:
            doc_type = ref.docutype
            citekey = ref.citekey

            print(f"\nType: {doc_type}, Citekey: {citekey}\n")
            for key, value in ref.bibDict.items():
                print(f"{key:10} {value}")
