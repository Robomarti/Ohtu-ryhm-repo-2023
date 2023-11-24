*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0.25 seconds
${HOME_URL}  http://${SERVER}
${ADD_REFERENCE_URL}  http://${SERVER}/add_reference
${LOGIN_URL}  http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    # Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Add Reference Page Should Be Open
    Title Should Be  Add reference

Go To Add Reference Page
    Go To  ${ADD_REFERENCE_URL}

Go To Home Page
    Go to  ${HOME_URL}

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Signin Page
    Go To  ${REGISTER_URL}

Should Be Logged In
    Go To Home Page
    Page Should Contain  References

Reference should be on Home Page
    [Arguments]  ${title}  ${author}  ${organization}  ${year}  ${source_type}  ${pages}  ${doi}
    Go To Home Page
    Page Should Contain  ${title}
    Page Should Contain  ${author}
    Page Should Contain  ${organization}
    Page Should Contain  ${year}
    Page Should Contain  ${source_type}
    Page Should Contain  ${pages}
    Page Should Contain  ${doi}