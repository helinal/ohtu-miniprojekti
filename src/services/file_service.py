
from config import BIBTEX_FILE_PATH

class File_Saver:
    def __init__(self,bib_repo=None):
        self.bib_repo = bib_repo

    def write(self):
        existing_references = self.bib_repo.fetch_all()
        refs_as_string = ''.join(existing_references)
        file_path = BIBTEX_FILE_PATH
        
        
        with open(file_path, 'w') as bib_file:
            bib_file.write(refs_as_string)


if __name__ == '__main__':
    filu = File_Saver()
    filu.write()