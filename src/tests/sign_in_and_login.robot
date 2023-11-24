*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Register User Succesfully
    Go To Signin Page
    Set Credentials  testi  robot
    Submit Signin Credentials
    Should Be Logged In

Loign Succesfully
    Go To Login Page
    Set Credentials  testi  robot
    Submit Login Credentials
    Should Be Logged In

*** Keywords ***
Set Credentials
    [Arguments]  ${username}  ${password}
    Input Text  username  ${username}
    Input Text  password  ${password}

Submit Login Credentials
    Click Button  Login

Submit Signin Credentials
    Click Button  Register