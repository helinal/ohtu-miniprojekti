import unittest
from services.doi_service import Doi_Service


class TestDoiService(unittest.TestCase):

    def setUp(self):
        self.doi_service = Doi_Service()

    def test_fetch_with_correct_doi(self):
        doi = '10.1016/S1574-0137(19)30321-1'
        data = self.doi_service.fetch(doi)
        self.assertEqual(
            data.entries[0]["title"], 'Introducing article numbering to Computer Science Review')

    def test_fetch_with_incorrect_doi(self):
        doi = 'moi'
        data = self.doi_service.fetch(doi)
        self.assertIsNone(data)
