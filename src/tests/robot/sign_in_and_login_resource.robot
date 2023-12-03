*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Set User Credentials
    [Arguments]  ${username}  ${password}
    Input Text  username  ${username}
    Input Text  password  ${password}

Submit Login Credentials
    Click Button  Login

Submit Signin Credentials
    Click Button  Register

Logout
    Go To Home Page
    Click Link  Logout

Signin As User
    [Arguments]  ${username}  ${password}
    Go To Signin Page
    Set User Credentials  ${username}  ${password}
    Submit Signin Credentials
    Should Be Logged In