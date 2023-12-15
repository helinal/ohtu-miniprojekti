*** Settings ***
Resource  resource.robot

*** Variables ***
@{CASE1INPUTS}=      3    Testi Tyyppi    Nimen Kirja    Kirjan Nimi    1969

*** Test Cases ***
App asks for a tag during manual reference input
    Input Add Command
    Loop Over Inputs For The Manual Test
    Input Nothing For A Number Of Times  11
    Input  testcase
    Input Stop Command
    Run Application
    Output Should Contain As Substring  tags (optional, separated by a comma): 

App asks for a tag during doi input
    Input DOI Command
    Input  10.4236/jcc.2015.34002
    Input  testcase
    Input Stop Command
    Run Application
    Output Should Contain As Substring  tags (optional, separated by a comma):

*** Keywords ***
Loop Over Inputs For The Manual Test
    FOR    ${thing}    IN    @{CASE1INPUTS}
        Input    ${thing}
    END