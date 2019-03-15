
Scenario Outline: Add new contact
	Given a contact list
	Given a contact with <lastname>,<firstname>,<address>,<email>,<email2>,<email3>,<home_phone>,<mobile_phone>,<work_phone> and <phone2>
	When I add the contact
	Then the new contact list is equal to the old list with the added contact

	Examples:
	| lastname    | firstname  | address    | email    | email2   | email3    | home_phone | mobile_phone | work_phone | phone2       |
    | lnameXSf2   | fname0Z8B  | addresslM  | email1_t | email2_m | email3_WJ | hphonew    | mphoneAAl    | wphonesZ0Z | phone2_cge2i |



Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact
    Then the new list is equal to the old list without the deleted contact



Scenario Outline: Change a contact
    Given a non-empty contact list
    Given a random contact from the list
    Given a contact with <lastname>,<firstname>,<address>,<email>,<email2>,<email3>,<home_phone>,<mobile_phone>,<work_phone> and <phone2>
    When I change the contact
    Then the new list is equal to the old list with changed contact

	Examples:
	| lastname    | firstname  | address    | email    | email2   | email3    | home_phone | mobile_phone | work_phone | phone2       |
    | lnameXSf23  | fname0Z83B | addresslM3 | email1_r | email2_g | email3_Wv | hphonew2   | mphoneAAle   | wphonesZ0f | phone2_cgew2 |