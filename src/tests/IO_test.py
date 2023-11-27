import unittest
from UI.ui import UI
from services.app_logic import AppLogic


class StubIO:
    def __init__(self, inputs: list):
        self.inputs = inputs
        self.outputs = []

    def read_input(self, text):
        return self.inputs.pop(0)

    def write_screen(self, text):
        self.outputs.append(text)


class TestUI(unittest.TestCase):
    def setUp(self):
        pass

    def test_start_and_insert_invalid_input(self):
        self.stub_io = StubIO(["4", "3"])
        self.ui = UI(self.stub_io)
        self.ui.start()

        expected_output = ["Invalid input, try again."]

        self.assertEqual(self.stub_io.outputs, expected_output)
    

    def test_start_and_insert_break_input(self):
        self.stub_io = StubIO(["3"])
        self.ui = UI(self.stub_io)
        self.ui.start()

        expected_output = []

        self.assertEqual(self.stub_io.outputs, expected_output)
    


