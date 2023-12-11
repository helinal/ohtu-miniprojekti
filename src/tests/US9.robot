*** Settings ***
Resource  resource.robot

*** Variables ***
@{CASE1INPUTS}=      3    Esim Erkki    ThisTitle    Robocop    1969
@{CASE2INPUTS}=      4    Mutsis Faija    Teesi    Tartu Ulikooli    1969

*** Test Cases ***
Inproceedings references save in inproceedings form
    Input Add Command
    Loop over inputs for the inproceedings test
    Input Nothing For A Number Of Times  12
    Input Print Command
    Input Stop Command
    Run Application
    Output Should Contain As Substring  Type: inproceedings

Phdthesis references save in phdthesis form
    Input Add Command
    Loop Over Inputs For The Phdthesis Test
    Input Nothing For A Number Of Times  6
    Input Print Command
    Input Stop Command
    Run Application
    Output Should Contain As Substring  Type: phdthesis

***Keywords***

Loop Over Inputs For The Inproceedings Test
    FOR    ${thing}    IN    @{CASE1INPUTS}
        Input    ${thing}
    END

Loop Over Inputs For The Phdthesis Test
    FOR    ${thing}    IN    @{CASE2INPUTS}
        Input    ${thing}
    END