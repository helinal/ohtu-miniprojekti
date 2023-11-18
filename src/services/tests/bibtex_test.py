import unittest
from bibtex import Bibtex


class TestBibtex(unittest.TestCase):
    def setUp(self):
        self.bibtex = Bibtex("article", "testref")

    def test_bibtex_init_works_correctly(self):
        s = str(self.bibtex)
        assert s == "@article{testref,\n}"

    def test_add_works_correctly(self):
        self.bibtex.add("year", "2000")
        s = str(self.bibtex)
        assert s == "@article{testref,\n    year = 2000\n}"