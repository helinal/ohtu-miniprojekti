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

Initialize database:

```bash
invoke build
```

Start program:

```bash
invoke start
```

## Usage:

### Adding a book:

- In the start menu, press _1_ and _Enter_ to start adding a reference
  - Type in _article_ or _book_ and press _Enter_
  - After adding the necessary filelds you can either skip or add a field. If you wish to skip a field, leave it empty and press _Enter_
- After adding the last field, the citation will be saved in BibTeX format to your local database

### Retrieving all the citations :

- Press _2_ and _Enter_ in the start menu to print out all the citations you have added
- The citations will automatically be printed in BibTeX format

### Resetting the database:

- Running `poetry run invoke build` after already initializing the database will clear it of all of its content

### Quit:

- Press _3_ in the start menu to exit the program

## Other command line actions:

_Run these commands in the root directory of this project_

> Note: If you wish to use these commands without typing poetry run every time you should enter the virtual environment by running the command `poetry shell`

Unittests:

```bash
poetry run invoke test
```

Robot:

```bash
poetry run invoke robot
```

Coverage:

```bash
poetry run invoke coverage
```

Coverage report:

```bash
poetry run invoke coverage-report
```

Open coverage report:

```bash
poetry run invoke coverage-open
```

Lint:

```bash
poetry run invoke lint
```

Format with autopep8:

```bash
poetry run invoke format
```
