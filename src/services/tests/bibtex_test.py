import unittest
from bibtex import Bibtex


classTestBibtex(unittest.TestCase):
    def setUp(self):
        self.bibtex = Bibtex("article", "testref")
    def test_bibtex_with_only_initial_values_returns_correctly(self):
        s = str(self.bibtex)
        assert(s == "@article\{testref,\n\}")