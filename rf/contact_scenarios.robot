*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  lnamef23  fname83B  addressM3  email1_e  email2_r  email3_v  hphonete  mphoneAle  wphone0f  phone2_ew2
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Modify contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${old_contact}=  Get From List  ${old_list}  ${index}
    ${new_contact}=  New ContactWithID  ${old_contact}  lnameCh  fnameCh  addressCh3  email1_C  email2_C  email3_C  hphoneCh  mphoneCh  wphoneCh  phone2_Ch
    Modify Contact  ${new_contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${old_contact}
    Insert Into List  ${old_list}  ${index}  ${new_contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}
