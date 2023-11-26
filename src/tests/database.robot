*** Settings ***
Resource  resource.robot
#Suite Setup  Connect DB
#Suite Teardown  Purge DB

*** Test Cases ***
User Can Save Article References To Database Succesfully
    Insert Article Reference    author    title    journal    1234
    Get References
    Output Should Contain    author,title,journal,1234

User Can Save Book References To Database Succesfully
    Insert Book Reference    author2    editor    title2    publisher    4321
    Get References
    Output Should Contain    author2,editor,title2,publisher,4321

References Are Stored In Database
    Insert Article Reference    author    title    journal    1234
    Insert Book Reference    author2    editor    title2    publisher    4321
    Disconnect DB
    Connect DB
    Get References
    Output Should Contain    author,author2

*** Keywords ***
Insert Article Reference
    [Arguments]  ${author}  ${title}  ${journal}  ${year}
    Input    ${author}
    Input    ${title}
    Input    ${journal}
    Input    ${year}
    Run Application

Insert Book Reference
    [Arguments]  ${author}  ${editor}  ${title}  ${publisher}  ${year}
    Input    ${author}
    Input    ${editor}
    Input    ${title}
    Input    ${publisher}
    Input    ${year}
    Run Application
    
Get References
    #TODO
