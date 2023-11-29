import unittest
from unittest.mock import Mock, ANY, patch
from services.app_logic import AppLogic
from services.bibtex import Bibtex


class TestAppLogic(unittest.TestCase):
    def setUp(self):
        self.bib_repo = Mock()
        self.app_logic = AppLogic(self.bib_repo)
        self.obj = Bibtex("entrytype")
        self.comparison_list = [self.obj]

    def test_initialize_citations(self):
        value = self.app_logic.initialize_citations()
        self.assertEqual(value, self.bib_repo.fetch_all())

    def test_return_all_citations(self):
        value = self.app_logic.return_all()
        comparison_value = self.bib_repo.fetch_all()
        self.assertEqual(value, comparison_value)

    def test_add_citation(self):
        self.app_logic.add(self.obj)
        value = self.app_logic.return_all()
        comparison_value = self.bib_repo.fetch_all()
        self.assertEqual(value, comparison_value)
