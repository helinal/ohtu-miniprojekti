import os
from stub_io import StubIO
from UI.ui import UI


class UILibrary:
    def __init__(self):
        self.io = StubIO()
        self.ui = UI(self.io)

    def input(self, value):
        self.io.add_input(value)

    def output_should_contain(self, value):
        outputs = self.io.outputs
        print(outputs)

        if not value in outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def output_should_not_contain_as_substring(self, value):
        outputs = self.io.outputs
        print(outputs)

        for member in outputs:
            if value in member:
                raise AssertionError(
                    f"Output \"{value}\" is not in {str(outputs)}"
                )

    def output_should_contain_as_substring(self, value):
        outputs = self.io.outputs
        print(outputs)

        found = False

        for member in outputs:
            if value in member:
                found = True

        if not found:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(outputs)}"
            )

    def file_exists_in_directory(self, file_name, target_directory):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        target_directory = os.path.join(current_directory, target_directory)
        file_path = os.path.join(target_directory, file_name)
        if not os.path.isfile(file_path):
            raise AssertionError(
                f"File \"{target_directory}/{file_name}\" does not exist."
            )

    def input_nothing_for_a_number_of_times(self, times):
        times = int(times)
        for i in range(times): #pylint: disable=unused-variable
            self.io.add_input("")

    def run_application(self):
        self.ui.start()
