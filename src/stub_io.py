class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write_screen(self, value):
        self.outputs.append(value)

    def read_input(self, prompt): # pylint: disable=unused-argument
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""

    def add_input(self, value):
        self.inputs.append(value)
