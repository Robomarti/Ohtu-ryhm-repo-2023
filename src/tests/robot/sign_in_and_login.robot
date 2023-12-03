*** Settings ***
Resource  resource.robot
Resource  sign_in_and_login_resource.robot
Suite Setup  Open And Configure Browser And Initialize Database
Suite Teardown  Close Browser

*** Test Cases ***
Register User Succesfully And Logout
    Go To Signin Page
    Set User Credentials  testi  Testaaja1lmar!
    Submit Signin Credentials
    Should Be Logged In
    Logout

Loign Succesfully And Logout
    Go To Login Page
    Set User Credentials  testi  Testaaja1lmar!
    Submit Login Credentials
    Should Be Logged In
    Logout