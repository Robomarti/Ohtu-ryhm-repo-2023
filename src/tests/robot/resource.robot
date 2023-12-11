*** Settings ***
Library  SeleniumLibrary
Library  AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0 seconds
${HOME_URL}  http://${SERVER}
${CHOOSE_SOURCE_TYPE_URL}  http://${SERVER}/choose_source_type
${LOGIN_URL}  http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser And Initialize Database
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}
    Initialize Database

Create Test Account And Login
    Create User  Testihyyppä  Testaaja1lmar!
    Go To Login Page
    Input Text  username  Testihyyppä
    Input Text  password  Testaaja1lmar!
    Click Button  Login

Login Page Should Be Open
    Page Should Contain  Login...

Register Page Should Be Open
    Page Should Contain  Create a new account:

Go To Home Page
    Go to  ${HOME_URL}

Go To Choose Source Type Page
    Go to  ${CHOOSE_SOURCE_TYPE_URL}

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Signin Page
    Go To  ${REGISTER_URL}

Should Be Logged In
    Go To Home Page
    Page Should Contain  References
