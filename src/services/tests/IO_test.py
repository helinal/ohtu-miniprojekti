import unittest
from unittest.mock import patch
from IO import KonsoliIO, UI


class TestKonsoliIO(unittest.TestCase):
    def setUp(self):
        self.konsoli_io = KonsoliIO()
        self.ui = UI()

    
    @patch('builtins.input', side_effect=["4"])
    def test_start_wrong_input(self, mock_input):
        result = self.ui.start()
        self.assertEqual(result, "invalid input, try again")