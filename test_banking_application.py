from banking_application import *
from clients import client_class
# '''The tests should be run on all functions in all the files. For banking application, it should be:
# -__return_client_df_as_dict
# -retrieving_a_client
# -accounts_with_negative_balance
# -deleting_a_client
# -changing_overdraft_limits
# -adding_a_client'''

import unittest

class test_banking_application(unittest.TestCase):

    def test_retrieving_a_client(self):
        banking_app_obj = Banking_Application()
        client_details = {
            "title": 'Mr',
            "first_name": 'Gerald',
            "last_name": 'Smith',
            "preferred_pronouns": 'he/him',
            "date_of_birth": '15/12/1990',
            "occupation": 'Software Engineer',
            "account_balance": 100,
            "overdraft_limit": 10
        }
        expected_client_object = client_class(**client_details)
        actual_response = banking_app_obj.retrieving_a_client("Gerald", "Smith", "15/12/1990")
        self.assertEqual(expected_client_object, actual_response)

class test_client_class(unittest.TestCase):

    def test_adding_in_account_balance(self):
        client_details = {
            "title": 'Mr',
            "first_name": 'Gerald',
            "last_name": 'Smith',
            "preferred_pronouns": 'he/him',
            "date_of_birth": '15/12/1990',
            "occupation": 'Software Engineer',
            "account_balance": 100,
            "overdraft_limit": 10
        }
        client_obj = client_class(**client_details)
        client_obj.adding_in_account_balance(100)
        client_dict = client_obj.return_client_dict()
        self.assertEqual(200, client_dict['Account Balance'][0])

#removing 150 to show what happens when the overdraft limit is exceeded.
    def test_removing_in_account_balance(self):
        client_details = {
            "title": 'Mr',
            "first_name": 'Gerald',
            "last_name": 'Smith',
            "preferred_pronouns": 'he/him',
            "date_of_birth": '15/12/1990',
            "occupation": 'Software Engineer',
            "account_balance": 100,
            "overdraft_limit": 10
        }
        client_obj = client_class(**client_details)
        client_obj.removing_in_account_balance(150)
        client_dict = client_obj.return_client_dict()
        self.assertEqual(-45, client_dict['Account Balance'][0])

    def test_changing_title(self):
        client_details = {
            "title": 'Mr',
            "first_name": 'Gerald',
            "last_name": 'Smith',
            "preferred_pronouns": 'he/him',
            "date_of_birth": '15/12/1990',
            "occupation": 'Software Engineer',
            "account_balance": 100,
            "overdraft_limit": 10
        }
        client_obj = client_class(**client_details)
        client_obj.changing_title("Mrs")
        client_dict = client_obj.return_client_dict()
        self.assertEqual("Mrs", client_dict['Title'][0])


    def test_changing_first_name(self):
        client_details = {
            "title": 'Mr',
            "first_name": 'Gerald',
            "last_name": 'Smith',
            "preferred_pronouns": 'he/him',
            "date_of_birth": '15/12/1990',
            "occupation": 'Software Engineer',
            "account_balance": 100,
            "overdraft_limit": 10
        }
        client_obj = client_class(**client_details)
        client_obj.changing_first_name("Harry")
        client_dict = client_obj.return_client_dict()
        self.assertEqual("Harry", client_dict['Firstname'][0])

    def test_changing_last_name(self):
        client_details = {
            "title": 'Mr',
            "first_name": 'Gerald',
            "last_name": 'Smith',
            "preferred_pronouns": 'he/him',
            "date_of_birth": '15/12/1990',
            "occupation": 'Software Engineer',
            "account_balance": 100,
            "overdraft_limit": 10
        }
        client_obj = client_class(**client_details)
        client_obj.changing_last_name("Lowe")
        client_dict = client_obj.return_client_dict()
        self.assertEqual("Lowe", client_dict['Lastname'][0])

    def test_changing_preferred_pronoun(self):
        client_details = {
            "title": 'Mr',
            "first_name": 'Gerald',
            "last_name": 'Smith',
            "preferred_pronouns": 'he/him',
            "date_of_birth": '15/12/1990',
            "occupation": 'Software Engineer',
            "account_balance": 100,
            "overdraft_limit": 10
        }
        client_obj = client_class(**client_details)
        client_obj.changing_preferred_pronoun("she/her")
        client_dict = client_obj.return_client_dict()
        self.assertEqual("she/her", client_dict['Pronouns'][0])

    def test_changing_occupation(self):
        client_details = {
            "title": 'Mr',
            "first_name": 'Gerald',
            "last_name": 'Smith',
            "preferred_pronouns": 'he/him',
            "date_of_birth": '15/12/1990',
            "occupation": 'Software Engineer',
            "account_balance": 100,
            "overdraft_limit": 10
        }
        client_obj = client_class(**client_details)
        client_obj.changing_occupation("Singer")
        client_dict = client_obj.return_client_dict()
        self.assertEqual("Singer", client_dict['Occupation'][0])


    def test_accounts_with_negative_balance(self):
        banking_app_obj = Banking_Application()
        actual_client_details = banking_app_obj.searching_for_accounts_with_negative_balance()
        expected = {'Title': {71: 'Mrs'}, 'Firstname': {71: 'Loy'}, 'Lastname': {71: 'Brewis'}, 'Pronouns': {71: 'he/him'}, 'Date of Birth': {71: '7/01/1955'}, 'Occupation': {71: 'Environmental Specialist'}, 'Account Balance': {71: -72798015}, 'Overdraft Limit': {71: 939400254}}
        self.assertEqual(expected,actual_client_details)

    def test_searching_by_firstname(self):
        banking_app_obj = Banking_Application()
        expected= {'Title': {95: 'Rev'}, 'Firstname': {95: 'Wilma'}, 'Lastname': {95: 'Huniwall'}, 'Pronouns': {95: 'they/them'}, 'Date of Birth': {95: '4/04/2000'}, 'Occupation': {95: 'Human Resources Assistant II'}, 'Account Balance': {95: 58438860}, 'Overdraft Limit': {95: 3867051}}
        actual_client= banking_app_obj.searching_by_firstname("Wilma")
        self.assertEqual(expected,actual_client)

    def test_searching_by_lastname(self):
        banking_app_obj = Banking_Application()
        expected = {'Title': {95: 'Rev'}, 'Firstname': {95: 'Wilma'}, 'Lastname': {95: 'Huniwall'}, 'Pronouns': {95: 'they/them'}, 'Date of Birth': {95: '4/04/2000'}, 'Occupation': {95: 'Human Resources Assistant II'}, 'Account Balance': {95: 58438860}, 'Overdraft Limit': {95: 3867051}}
        actual_client = banking_app_obj.searching_by_lastname("Huniwall")
        self.assertEqual(expected, actual_client)

    def test_searching_by_date_of_birth(self):
        banking_app_obj = Banking_Application()
        expected = {'Title': {80: 'Mrs'}, 'Firstname': {80: 'Delphine'}, 'Lastname': {80: 'Neiland'}, 'Pronouns': {80: 'she/her'}, 'Date of Birth': {80: '10/04/1979'}, 'Occupation': {80: 'VP Marketing'}, 'Account Balance': {80: 414546988}, 'Overdraft Limit': {80: 55133275}}
        actual_client = banking_app_obj.searching_by_date_of_birth("10/04/1979")
        self.assertEqual(expected, actual_client)

    def test_changing_overdraft_limits(self):
        banking_app_obj = Banking_Application()





