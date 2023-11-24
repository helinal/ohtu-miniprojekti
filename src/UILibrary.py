from stub_io import StubIO
from UI.ui import UI

class UILibrary:
    def __init__(self):
        self.io = StubIO()
        self.ui = UI(self.io)

    def input(self, value):
        self.io.add_input(value)

    def output_should_contain(self, value):
        outputs = self._io.outputs

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def run_application(self):
        self.ui.start()