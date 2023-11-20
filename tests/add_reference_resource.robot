*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Keywords ***
Set Reference
    [Arguments]  ${title}  ${author}  ${organization}  ${year}  ${source_type}  ${pages}  ${doi}
    Input Text  title  ${title}
    Input Text  author  ${author}
    Input Text  organization  ${organization}
    Input Text  year  ${year}
    Input Text  source_type  ${source_type}
    Input Text  pages  ${pages}
    Input Text  doi  ${doi}

Submit Reference Credentials
    Click Button  Add reference
