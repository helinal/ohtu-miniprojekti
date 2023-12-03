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
        self.outputs.append(text.__str__())
    
    def print_readable_form(self, text):
        self.outputs.append('reference')

class TestUI(unittest.TestCase):
    def setUp(self):
        pass

    def test_start_and_insert_invalid_input(self):
        self.stub_io = StubIO(["asd", "5"])
        self.ui = UI(self.stub_io)
        self.ui.start()

        expected_output = ["Invalid input, try again."]

        self.assertEqual(self.stub_io.outputs, expected_output)

    def test_start_and_insert_break_input(self):
        self.stub_io = StubIO(["5"])
        self.ui = UI(self.stub_io)
        self.ui.start()

        expected_output = []

        self.assertEqual(self.stub_io.outputs, expected_output)

    def test_try_to_add_non_supported_docutype(self):
        self.stub_io = StubIO(["1", "999","5","5"])
        self.ui = UI(self.stub_io)
        self.ui.start()

        expected_output = ["Invalid input, try again."]

        self.assertEqual(self.stub_io.outputs, expected_output)

    def test_add_article_with_empty_author_and_print_all(self):
        self.stub_io = StubIO(["1", "1","","asd","asd","asd",'123',"","","","","","2","5"])
        self.ui = UI(self.stub_io)
        self.ui.start()

        print("1st dbtest:")
        print(self.stub_io.outputs)

        expected_output = "Invalid input, try again."

        self.assertEqual(self.stub_io.outputs[0], expected_output)
        self.assertEqual(len(self.stub_io.outputs), 2)

    def test_add_book_with_bad_year_and_print_all(self):
        self.stub_io = StubIO(["1", "2", "author", "editor", "title",
                              "publisher", "year", "2000", "", "", "", "february", "", "2", "5"])
        self.ui = UI(self.stub_io)
        self.ui.start()

        expected_output = "Year needs to be only numbers, try again."

        print("3rd dbtest:")
        print(self.stub_io.outputs)

        self.assertEqual(self.stub_io.outputs[0], expected_output)
