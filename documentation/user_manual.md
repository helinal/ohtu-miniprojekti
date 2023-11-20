# User manual

## Start:

Clone this repository to your computer:

```bash
git clone git@github.com:helinal/ohtu-miniprojekti.git
```

In the root directory, run this command to install the dependencies:

```bash
poetry install
```

Enter Poetry's virtual environment:

```bash
poetry shell
```

Start program:

```bash
python3 src/services/index.py
```

## Usage:

### Adding a book:

- In the start menu, press _1_ and _Enter_ to start adding a book
- After adding the last field, the citation will be saved in BibTeX format

### Retrieving all the citations :

- Press _2_ and _Enter_ in the start menu to print out all the citations you have added
- The citations will automatically be printed in BibTeX format

### Quit:

- Press _3_ in the start menu to exit the program

## Command line actions:

_Run these commands in the root directory of this project_

> Note: If you wish to use these commands without typing poetry run every time you should enter the virtual environment by running the command `poetry shell`

Unittests:

```bash
poetry run pytest src/services/tests/
```

Coverage:

```bash
poetry run coverage run --branch -m pytest
```

After running the command above, see coverage report by running:

```bash
poetry run coverage report -m
```

Generate and open coverage html file:

```bash
poetry run coverage html
```

```bash
open htmlcov/index.html
```

Lint:

```bash
poetry run pylint src
```
