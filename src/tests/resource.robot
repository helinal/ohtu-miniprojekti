*** Settings ***
Library  ../UILibrary.py


*** Keywords ***

Start Application
    Run Application
   
Input Add Command
    Input  1

Input Print Command
    Input  2

Input Save Command
    Input  3

Input DOI Command
    Input  4

Input Stop Command
    Input  7
