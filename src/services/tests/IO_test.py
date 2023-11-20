import unittest
from unittest.mock import patch
from IO import UI, KonsoliIO


#class TestUI(unittest.TestCase):
#    def setUp(self):
#        self.ui = UI()
#        self.konsoli_io = KonsoliIO()
#
#    @patch('builtins.input', return_value=["4"])
#    def test_start(self, mock_input):
#        result = self.ui.start()
#        self.assertEqual(result, "invalid input, try again")