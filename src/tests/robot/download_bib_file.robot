*** Settings ***
Library  OperatingSystem
Resource  resource.robot
Suite Setup  Open And Configure Browser Initialize Database And Signin
Suite Teardown  Close Browser

*** Variables ***
${downloads_path}  ~/Downloads/references.bib

*** Test Cases ***
Downloading Bib File Works
    Click Button  Download File
    Sleep  5s
    File Should Exist  ${downloads_path}

*** Keywords ***
Open And Configure Browser Initialize Database And Signin
    Open And Configure Browser And Initialize Database
    Create Test Account And Login

