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

Add Article Page Should Be Open
    Title Should Be  Add article

Choose Source Type Page Should Be Open
    Title Should Be  Choose source type

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

Article should be on Home Page
    [Arguments]  ${author}  ${title}  ${journal}  ${year}  ${volume}  ${number}  ${pages}
    Go To Home Page
    Page Should Contain  ${author}
    Page Should Contain  ${title}
    Page Should Contain  ${journal}
    Page Should Contain  ${year}
    Page Should Contain  ${volume}
    Page Should Contain  ${number}
    Page Should Contain  ${pages}

Book should be on Home Page
    [Arguments]  ${author}  ${title}  ${publisher}  ${address}  ${year}
    Go To Home Page
    Page Should Contain  ${author}
    Page Should Contain  ${title}
    Page Should Contain  ${publisher}
    Page Should Contain  ${address}
    Page Should Contain  ${year}

Inproceedings should be on Home Page
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
    