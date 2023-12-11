import unittest
from unittest.mock import patch, Mock
import requests
from services.doi_service import DoiService


class TestDoiService(unittest.TestCase):

    def setUp(self):
        self.doi_service = DoiService()

    def test_fetch_with_correct_doi(self):
        doi = '10.1016/S1574-0137(19)30321-1'
        data = self.doi_service.fetch(doi)
        self.assertEqual(
            data.entries[0]["title"], 'Introducing article numbering to Computer Science Review')

    def test_fetch_with_incorrect_doi(self):
        doi = 'moi'
        data = self.doi_service.fetch(doi)
        self.assertIsNone(data)

    @patch('requests.get')
    def test_fetch_timeout(self, mock_get):
        mock_get.side_effect = requests.Timeout
        result = self.doi_service.fetch('10100010/ha')
        self.assertIsNone(result)
        mock_get.assert_called_once_with(
            'https://dx.doi.org//10100010/ha', headers={"accept": "application/x-bibtex"}, timeout=10)
