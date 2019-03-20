*** Settings ***
Library        web_driver//EnquiryFormHelper.py      Chrome
Suite Setup     Open
Suite Teardown  Close

*** Test Cases ***
The user can fill us the enquiry form
    click customize button
    enter name   test_sarthak
    enter phone    1111111111
    enter email    test@sarthak.com
    select no of people  2
    select trip begin   In this week
    select trip location     Bali
    select random date