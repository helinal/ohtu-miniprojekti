class StubIO:
    def __init__(self, inputs=None):
<<<<<<< HEAD

        self.inputs = inputs

        self.outputs = []

    def read_input(self, text):

        return self.inputs.pop(0)

    def write_screen(self, text):

        self.outputs.append(text)
=======
        self.inputs = inputs or []
        self.outputs = []

    def write_screen(self, value):
        self.outputs.append(value)

    def read_input(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return ""
>>>>>>> d414b0d (robo)

    def add_input(self, value):
        self.inputs.append(value)
