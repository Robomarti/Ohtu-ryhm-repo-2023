*** Settings ***
Resource  resource.robot
Resource  add_reference_resource.robot
Resource  sign_in_and_login_resource.robot
Suite Setup  Open And Configure Browser Initialize Database And Signin
Suite Teardown  Close Browser

*** Test Cases ***
Add Valid Article
    Open Choose Source Type Page And Input Type  article
    Set Article  Arno  Testi  Testimesta  2023  1  2  100
    Add Reference And Go To Home Page
    Article should be on Home Page  Arno  Testi  Testimesta  2023  1  2  100

Add Valid Book
    Open Choose Source Type Page And Input Type  book
    Set Book  Kolli  Pesti  Testaajat  Jossain Tuolla  1995
    Add Reference And Go To Home Page
    Book should be on Home Page  Kolli  Pesti  Testaajat  Jossain Tuolla  1995

Add Valid Inproceedings
    Open Choose Source Type Page And Input Type  inproceedings
    Set Inproceedings  Aku Ankka  Ankkalinnan Mestari  Epäonninen  Köyhät  2015  253  Roopen Posse  Ankkakatu 2
    Add Reference And Go To Home Page
    Inproceedings should be on Home Page  Aku Ankka  Ankkalinnan Mestari  Epäonninen  Köyhät  2015  253  Roopen Posse  Ankkakatu 2

*** Keywords ***
Add Reference And Go To Home Page
    Submit Reference Credentials

Open Choose Source Type Page And Input Type
    [Arguments]  ${type}
    Go To Choose Source Type Page
    Choose Source Type  ${type}

Open And Configure Browser Initialize Database And Signin
    Open And Configure Browser And Initialize Database
    Create Test Account And Login
    