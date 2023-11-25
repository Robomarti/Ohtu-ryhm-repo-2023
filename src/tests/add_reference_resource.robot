*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Set Article
    [Arguments]  ${author}  ${title}  ${journal}  ${year}  ${volume}  ${number}  ${pages}
    Input Text  author  ${author}
    Input Text  title  ${title}
    Input Text  journal  ${journal}
    Input Text  year  ${year}
    Input Text  volume  ${volume}
    Input Text  number  ${number}
    Input Text  pages  ${pages}

Submit Reference Credentials
    Click Button  Add
