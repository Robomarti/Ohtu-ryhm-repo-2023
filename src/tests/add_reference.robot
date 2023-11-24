*** Settings ***
Resource  resource.robot
Resource  add_reference_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add Reference Page

*** Test Cases ***
Add Valid Reference
    Set Reference  testi  Arno  Testimesta Org  2023  Book  5  mikaondoi
    Add Reference And Go To Home Page
    Reference should be on Home Page  testi  Arno  Testimesta Org  2023  Book  5  mikaondoi

*** Keywords ***
Add Reference And Go To Home Page
    Submit Reference Credentials
    Go To Home Page
