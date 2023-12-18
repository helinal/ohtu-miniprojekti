# ohtu-miniprojekti

[Product and sprint backlog](https://docs.google.com/spreadsheets/d/1uLXQf_AoPL6ly2yu5XrqHldBCUcM7QaakHexxE-Yq5s/edit#gid=0)

[User manual](https://github.com/helinal/ohtu-miniprojekti/blob/main/documentation/user_manual.md)

![GHA workflow badge](https://github.com/helinal/ohtu-miniprojekti/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/helinal/ohtu-miniprojekti/graph/badge.svg?token=71GPV9BTFQ)](https://codecov.io/gh/helinal/ohtu-miniprojekti)

### Sprint 4

#### Definition of done

The following user stories are completed according to acceptance criteria:

##### As a user I can delete a reference
 - Application asks user if they want to delete a reference.
 - Application deletes the reference from db.

##### As a user I can add tags to references
 - Application asks user if they want to put all references into a file.
 - All data goes from db to a .bib file.

##### As a user I can search references
 - Application asks user if they want to search references with a tag.
 - Application fetches the references by tag if found.


The completion of user stories is verified through extensive unit testing across the program. The user story 'As a user I can add tags to references' is also system tested according to acceptance criteria.
The program is continuosly integrated. Program releases contain a high unit testing coverage with fully passing unit and system tests.

### Sprint 3

#### Definition of done

The following user stories are completed according to acceptance criteria:

##### As a user I can print references to a file
 - Application asks user if they want to put all references into a file.
 - All data goes from db to a .bib file

##### As a user I can list references in readable form
 - Printing to terminal prints in a human readable form, rather than BibTeX.

##### As a user I can add a new reference based on doi
 - Application has an option for inputting a doi references.
 - Application fetches a reference by doi and saves it to the database.

##### As a user I can add inproceedings and phdthesis references in the system
 - Inproceedings references are saved in inproceedings form.
 - Phdthesis references are save in phdthesis form.


The completion of user stories is verified through extensive unit testing across the program, and by system testing each added story according to acceptance criteria.
The program is continuosly integrated. Program releases contain a high unit testing coverage with fully passing unit and system tests.


### Sprint 2

#### Definition of done

The following user stories are completed according to acceptance criteria:

##### As a user I can save references on my computer
 - Inputted data is saved locally.
 - Program writes and reads into a SQLite database.

##### As a user I can add book references into the system
 - Application asks user for a reference type for input.
 - Book references are saved in book type bibtex format.

##### As a user I can add both mandatory and optional fields
 - Application form has optional fields, which are clearly annotated.
 - A reference with invalid mandatory fields is not accepted.
 - Optional fields can be left empty.

The completion of user stories is verified through extensive unit testing across the program, and system testing is begun during this sprint.
The program is continuosly integrated, with test coverage and passing kept high throughout development.



### Sprint 1

#### Definition of done

The following user stories are completed according to acceptance criteria:

##### As a user I can add article references by filling a form in terminal
 - Application asks user if they want to input data.
 - Input form asks user for values required for an article reference.

##### As a user I can print all the references in the terminal in a bibtex form
 - Inputted data is kept as long as the program is open.
 - Application asks user if they want to print all references inputted.
 - References are printed to terminal in BibTeX form.

The completion of user stories is verified through unit testing across non-IO layers of the program.
In addition, the program is continuosly integrated, with test coverage and passing kept high throughout development.


