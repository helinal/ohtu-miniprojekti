*** Settings ***
Resource  resource.robot
Test Setup  Start Application

*** Test Cases ***

User Can Fill Book References With Right Inputs
    Input Book Command
    Insert Book Reference Mandatory  1234  henni  moi  ii  moi  1234
    Insert Book Reference Optional  moi  12  1234  04  jeee
    Input 3 Command
    
#User Can Fill Book References With Wrong Inputs



*** Keywords ***

Start Application
    Run Application
    Input 1 Command

Input 1 Command
    Input  "1"

Input 3 Command
    Input  "3"

Input Book Command
    Input  "book"

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
    

