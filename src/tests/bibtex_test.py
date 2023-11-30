from services.bibtex import Bibtex
import unittest


class TestBibtex(unittest.TestCase):
    def setUp(self):
        self.bibtex_instance = Bibtex("article")

    def test_create_citekey(self):
        self.bibtex_instance.bibDict["author"] = "Kalle"
        self.bibtex_instance.bibDict["year"] = 2023
        self.bibtex_instance.create_citekey()
        self.assertEqual(self.bibtex_instance.citekey, "Kalle2023")

    def test_loop_to_string(self):
        self.bibtex_instance.bibDict = {
            "author": "Helina", "title": "Example", "year": 2021}
        result = self.bibtex_instance.loop_to_string()
        expected = ",\n    author = \"Helina\",\n    title = \"Example\",\n    year = 2021"
        self.assertEqual(result, expected)

    def test_str(self):
        self.bibtex_instance.bibDict = {
            "author": "Henni", "title": "Example", "year": 2021}
        self.bibtex_instance.create_citekey()
        result = str(self.bibtex_instance)
        expected = "@article{Henni2021,\n    author = \"Henni\",\n    title = \"Example\",\n    year = 2021\n}"
        self.assertEqual(result, expected)

    def test_add(self):
        self.bibtex_instance.add("Kumpula", "Journal of Examples")
        self.assertEqual(
            self.bibtex_instance.bibDict["Kumpula"], "Journal of Examples")
