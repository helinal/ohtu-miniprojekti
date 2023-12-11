*** Settings ***
Resource  resource.robot

*** Test Cases ***
Application has an option for inputting a doi references
    Input DOI Command
    Input  http://dx.doi.org/10.1093/ajae/aaq063
    Input Print Command
    Input Stop Command
    Run Application
    Output Should Contain As Substring  Enter DOI:

Application fetches a reference by doi and saves it to the database.
    Input DOI Command
    Input  http://dx.doi.org/10.1093/ajae/aaq063
    Input Nothing For A Number Of Times  1
    Input Print Command
    Input Stop Command
    Run Application
    Output Should Contain As Substring  An Analysis of the Pricing of Traits in the U.S. Corn Seed Market
