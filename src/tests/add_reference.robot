*** Settings ***
Resource  resource.robot
Resource  add_reference_resource.robot
Resource  sign_in_and_login_resource.robot
Suite Setup  Open And Configure Browser And Initialize Database
Suite Teardown  Close Browser
Test Setup  Signin As User  Referenssi  testaaja

*** Test Cases ***
Add Valid Article
    Go To Add Article Page
    Set Article  Arno  Testi  Testimesta  2023  1  2  100
    Add Reference And Go To Home Page
    Article should be on Home Page  Arno  Testi  Testimesta  2023  1  2  100

*** Keywords ***
Add Reference And Go To Home Page
    Submit Reference Credentials
    Go To Home Page
