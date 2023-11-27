*** Settings ***
Resource  resource.robot

*** Test Cases ***

User Can Fill Book References With Right Inputs
    Input 1 Command
    Input Book Command
    Insert Book Reference Mandatory  1234  henni  editor  kirja  julkaisija  1980
    Insert Book Reference Optional  3  12  1234  04  hyvä
    Input 3 Command
    
User Can Fill Book References With Wrong Inputs
    Input 1 Command
    Input Book Command
    Insert Book Reference Mandatory  1234  henni  editor  kirja  julkaisija  moi
    Output Should Contain    Year needs to be only numbers, try again
    Insert Year  1980
    Insert Book Reference Optional  3  12  1234  04  hyvä
    Input 3 Command
    



*** Keywords ***

Start Application
    Run Application
   
Input 1 Command
    Input  "1"

Input 3 Command
    Input  "3"

Input Book Command
    Input  "book"

Insert Year
    [Arguments]  ${year}
    Input    ${year}


Insert Book Reference Mandatory
    [Arguments]  ${citekey}  ${author}  ${editor}  ${title}  ${publisher}  ${year}
    Input    ${citekey}
    Input    ${author}
    Input    ${editor}
    Input    ${title}
    Input    ${publisher}
    Input    ${year}

Insert Book Reference Optional
    [Arguments]  ${volume}  ${number}  ${pages}  ${month}  ${note}
    Input    ${volume}
    Input    ${number}
    Input    ${pages}
    Input    ${month}
    Input    ${note}
    

