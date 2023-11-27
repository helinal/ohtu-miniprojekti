class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write_screen(self, value):
        self.outputs.append(value)

    def read_input(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""

    def add_input(self, value):
        self.inputs.append(value)
