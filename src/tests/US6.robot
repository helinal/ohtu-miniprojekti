*** Settings ***
Resource  resource.robot

*** Test Cases ***
Application asks user if they want to put all references into a file

    Input Stop Command
    Run Application
    Output Should Contain As Substring  to save references to file

All data goes from db to a .bib file
    Input Save Command
    Input Stop Command
    Run Application
    Output Should Contain  References saved to file. References can be found in src/data/bibtex.bib
