*** Settings ***
Library SeleniumLibrary
Resource  resource.robot
Resource  add_reference_resource.robot
Suite Setup  Open And Configure Browser Initialize Database And Signin
Suite Teardown  Close Browser

*** Test Cases ***
Logged In User Sees BibTeX Data
    Click Button  BibTeX
    Page Should Contain  References in BibTeX form
    Page Should Contain  author = "Mina",
    Page Should Contain  title = "Kirja",
    Page Should Contain  publisher = "Testaajat",
    Page Should Contain  address = "Jossain Tuolla",
    Page Should Contain  year = 2000

Logged In User Sees Normal Data
    Click Button  Text
    Page Should Contain  References
    Page Should Not Contain  in BibTeX form
    Page Contains  Author:  Mina
    Page Contains  Title:  Kirja
    Page Contains  Publisher:  Testaajat
    Page Contains  Year:  2000

*** Keywords ***
Open And Configure Browser Initialize Database And Signin
    Open And Configure Browser And Initialize Database
    Create Test Account And Login
    Open Choose Source Type Page And Input Type  book
    Set Book  Mina  Kirja  Testaajat  Jossain Tuolla  2000
    Add Reference And Go To Home Page

Add Reference And Go To Home Page
    Submit Reference Credentials

Open Choose Source Type Page And Input Type
    [Arguments]  ${type}
    Go To Choose Source Type Page
    Choose Source Type  ${type}

Page Contains
    [Arguments]  ${type}  ${value}
    Page Should Contain  ${type}
    Page Should Contain  ${value}