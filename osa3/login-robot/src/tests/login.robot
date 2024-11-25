*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in



Login With Inorrect Credentials
    Input Credentials  kalle  kalle000
    Output Should Contain  Invalid username or password


Login With Nonexistent Username
    Input Credentials  kallee  kalle123
    Output Should Contain  Invalid username or password


*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input Login Command
