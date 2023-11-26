class StubIO:
    def __init__(self, inputs=None):

        self.inputs = inputs

        self.outputs = []

    def read_input(self, text):

        return self.inputs.pop(0)

    def write_screen(self, text):

        self.outputs.append(text)

    def add_input(self, value):
        self.inputs.append(value)
