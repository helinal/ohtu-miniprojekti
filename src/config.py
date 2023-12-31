import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

DATABASE_FILE = os.getenv('DATABASE_FILE') or 'db.sqlite'
DATABASE_FILE_PATH = os.path.join(dirname, "data", DATABASE_FILE)

BIBTEX_FILE = os.getenv('BIBTEX_FILE') or 'bibtex.bib'
BIBTEX_FILE_PATH = os.path.join(dirname, 'data', BIBTEX_FILE)
