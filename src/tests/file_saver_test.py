import unittest
from unittest.mock import Mock, patch
from services.file_service import File_Saver  # replace with the actual module name

class TestFileSaver(unittest.TestCase):
    def setUp(self):
        self.mock_bib_repo = Mock()
        self.file_saver = File_Saver(bib_repo=self.mock_bib_repo)

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_write(self, mock_open):
        mock_objects = [Mock(), Mock()]
        self.mock_bib_repo.fetch_all.return_value = mock_objects

        self.file_saver.write()

        mock_file_handle = mock_open()
        self.mock_bib_repo.fetch_all.assert_called_once()
        mock_file_handle.write.assert_called_once_with('\n'.join(str(obj) for obj in mock_objects))