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

Register As
    [Arguments]  ${username}  ${password}
    Go To Signin Page
    Set User Credentials  ${username}  ${password}
    Submit Signin Credentials

Login As
    [Arguments]  ${username}  ${password}
    Go To Login Page
    Set User Credentials  ${username}  ${password}
    Submit Login Credentials

Wont Allow Logging In And Login Page Contains Error Message
    Login Page Should Be Open
    Page Should Contain  Invalid credentials.