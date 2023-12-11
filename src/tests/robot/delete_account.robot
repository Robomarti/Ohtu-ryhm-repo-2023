*** Settings ***
Resource  resource.robot
Resource  sign_in_and_login_resource.robot
Suite Setup  Open And Configure Browser And Initialize Database
Suite Teardown  Close Browser

*** Test Cases ***
Canceling User Account deletion Does Not Delete Account
    Create Test Account And Login
    Should Be Logged In
    Go To Account Removal Page
    Click Button  Changed my mind, return to main page
    Should Be Logged In
    Logout
    Login As  Testihyyppä  Testaaja1lmar!
    Should Be Logged In

Deleting User Account Logsout User And Redirects To Login Page
    Go To Account Removal Page
    Click Button  Permanently Delete Account
    Login Page Should Be Open

Cant Login To Deleted User Account
    Login As  Testihyyppä  Testaaja1lmar!
    Wont Allow Logging In And Login Page Contains Error Message

*** Keywords ***
Go To Account Removal Page
    Click Link  Remove Account
    Page Should Contain  Caution! By proceeding, you are requesting the permanent deletion of your user account and all saved data.
