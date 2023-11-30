
from config import BIBTEX_FILE_PATH


class File_Saver:
    def __init__(self, bib_repo=None):
        self.bib_repo = bib_repo

    def write(self):
        existing_references = self.bib_repo.fetch_all()
        string_list = [str(obj) for obj in existing_references]

        refs_as_string = '\n'.join(string_list)
        file_path = BIBTEX_FILE_PATH

        with open(file_path, 'w', encoding='utf-8') as bib_file:
            bib_file.write(refs_as_string)

        return "References saved to file. References can be found in src/data/bibtex.bib"
