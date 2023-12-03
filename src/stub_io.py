class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write_screen(self, value):
        self.outputs.append(value)

    def read_input(self, prompt):  # pylint: disable=unused-argument
        self.outputs.append(prompt)
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""

    def add_input(self, value):
        self.inputs.append(value)

    def print_readable_form(self, text):
        to_print = ""
        if not text:
            to_print += "\nYou do not have any references to print!\n"

        for i in text:
            doc_type = i.docutype
            citekey = i.citekey

            to_print += f"\nType: {doc_type}, Citekey: {citekey}\n"
            for key, value in i.bibDict.items():
                to_print += f"{key:10} {value}"

        self.outputs.append(to_print)
