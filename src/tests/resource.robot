*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0.25 seconds
${HOME_URL}  http://${SERVER}
${ADD_ARTICLE_URL}  http://${SERVER}/add_article
${LOGIN_URL}  http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register
${DB_INITIALIZE_URL}  http://${SERVER}/db_initialize

*** Keywords ***
Open And Configure Browser And Initialize Database
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}
    Initialize Database

Initialize Database
    Go To  ${DB_INITIALIZE_URL}

Add Article Page Should Be Open
    Title Should Be  Add article

Go To Add Article Page
    Go To  ${ADD_ARTICLE_URL}

Go To Home Page
    Go to  ${HOME_URL}

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