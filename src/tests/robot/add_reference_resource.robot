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

Set Book
    [Arguments]  ${author}  ${title}  ${publisher}  ${address}  ${year}
    Input Text  author  ${author}
    Input Text  title  ${title}
    Input Text  publisher  ${publisher}
    Input Text  address  ${address}
    Input Text  year  ${year}

Set Inproceedings
    [Arguments]  ${author}  ${title}  ${booktitle}  ${series}  ${year}  ${pages}  ${publisher}  ${address}
    Input Text  author  ${author}
    Input Text  title  ${title}
    Input Text  booktitle  ${booktitle}
    Input Text  series  ${series}
    Input Text  year  ${year}
    Input Text  pages  ${pages}
    Input Text  publisher  ${publisher}
    Input Text  address  ${address}

Submit Reference Credentials
    Click Button  Add

Choose Source Type
    [Arguments]  ${type}
    Select From List By Value  name:source_type  ${type}
    Click Button  Select type

Article Should Be On Home Page
    [Arguments]  ${author}  ${title}  ${journal}  ${year}  ${volume}  ${number}  ${pages}
    Go To Home Page
    Page Should Contain  ${author}
    Page Should Contain  ${title}
    Page Should Contain  ${journal}
    Page Should Contain  ${year}
    Page Should Contain  ${volume}
    Page Should Contain  ${number}
    Page Should Contain  ${pages}

Book Should Be On Home Page
    [Arguments]  ${author}  ${title}  ${publisher}  ${address}  ${year}
    Go To Home Page
    Page Should Contain  ${author}
    Page Should Contain  ${title}
    Page Should Contain  ${publisher}
    Page Should Contain  ${address}
    Page Should Contain  ${year}

Inproceedings Should Be On Home Page
    [Arguments]  ${author}  ${title}  ${booktitle}  ${series}  ${year}  ${pages}  ${publisher}  ${address}
    Go To Home Page
    Page Should Contain  ${author}
    Page Should Contain  ${title}
    Page Should Contain  ${booktitle}
    Page Should Contain  ${series}
    Page Should Contain  ${year}
    Page Should Contain  ${pages}
    Page Should Contain  ${publisher}
    Page Should Contain  ${address}
