*** Settings ***
Resource  resource.robot
Test Setup 

*** Variables ***
@{INPUTS}=      3    Esim Erkki    ThisTitle    Robocop    1969

*** Test Cases ***
Application lists references in a readable form    
    Input Add Command
    Loop over Inputs
    Input Nothing For A Number Of Times  11
    Input Print Command
    Input Stop Command
    Run Application
    Output Should Not Contain As Substring  @
    Output Should Not Contain As Substring  {
    Output Should Not Contain As Substring  }
    
***Keywords***

Loop Over Inputs
    FOR    ${thing}    IN    @{INPUTS}
        Input    ${thing}
    END
