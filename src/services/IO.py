class KonsoliIO():
    def read_input(self, text):
        return input(text)

    def write_screen(self, text):
        print(text)

    def print_readable_form(self, text):
        if not text:
            print("\nYou do not have any refences to print!\n")

        for i in text:
            doc_type = i.docutype
            citekey = i.citekey

            print(f"\nType: {doc_type}, Citekey: {citekey}\n")
            for key, value in i.bibDict.items():
                print(f"{key:10} {value}")
