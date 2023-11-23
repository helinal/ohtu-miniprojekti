import unittest
from services.app_logic import AppLogic
from services.bibtex import Bibtex


class TestAppLogic(unittest.TestCase):
    def setUp(self):
        self.app_logic = AppLogic()
        self.obj = Bibtex("entrytype", "cite")
        self.comparison_list = [self.obj]

    def test_constructor(self):
        self.assertEqual(self.app_logic.citations, [])
        self.assertEqual(self.comparison_list, [self.obj])

    def test_add(self):
        self.app_logic.add(self.obj)
        self.assertEqual(self.comparison_list, self.app_logic.citations)

    def test_return_all(self):
        self.app_logic.add(self.obj)
        self.assertEqual(self.comparison_list, self.app_logic.return_all())
