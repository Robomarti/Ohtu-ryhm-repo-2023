*** Settings ***
Resource  resource.robot
Resource  add_reference_resource.robot
Resource  sign_in_and_login_resource.robot
Suite Setup  Open And Configure Browser Initialize Database And Signin
Suite Teardown  Close Browser

*** Test Cases ***
Deleting Articles Works
    Go To Home Page
    Delete Reference And Check If Its Deleted  Writer 1
    Delete Reference And Check If Its Deleted  Writer 2
    Page Should Contain  You don't have any saved articles.

Deleting Books Works
    Delete Reference And Check If Its Deleted  Tester 1
    Delete Reference And Check If Its Deleted  Tester 2
    Page Should Contain  You don't have any saved books.

Deleting Inproceedings Works
    Delete Reference And Check If Its Deleted  Author1
    Delete Reference And Check If Its Deleted  Author2
    Page Should Contain  You don't have any saved inproceedings.

*** Keywords ***
Open And Configure Browser Initialize Database And Signin
    Open And Configure Browser And Initialize Database
    Create Test Account And Login

Delete Reference And Check If Its Deleted
    [Arguments]  ${locator}
    Page Should Contain  ${locator}
    Mouse Over  class:source
    Click Button  Delete
    Page Should Not Contain  ${locator}
