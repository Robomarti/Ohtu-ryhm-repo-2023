*** Settings ***
Resource  resource.robot
Resource  add_reference_resource.robot
Suite Setup  Open And Configure Browser Initialize Database And Signin
Suite Teardown  Close Browser

*** Test Cases ***
Logged In User Sees BibTeX Data
    Click Button  BibTeX
    Page Should Contain  References in BibTeX form
    Click Button  Text
    Page Should Contain  References

*** Keywords ***
Open And Configure Browser Initialize Database And Signin
    Open And Configure Browser And Initialize Database
    Create Test Account And Login
    Open Choose Source Type Page And Input Type  book
    Set Book  Kolli  Pesti  Testaajat  Jossain Tuolla  1995
    Add Reference And Go To Home Page

Add Reference And Go To Home Page
    Submit Reference Credentials

Open Choose Source Type Page And Input Type
    [Arguments]  ${type}
    Go To Choose Source Type Page
    Choose Source Type  ${type}