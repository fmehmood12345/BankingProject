from banking_application import *
from clients import client_class
# from nose.tools import assert_dict_equal
# def test_accounts_with_negative_balance():
#     BA_Obj = Banking_Application()
#     x = BA_Obj.accounts_with_negative_balance()
#     expected = {
#         "Title": 'Honorable',
#         "Firstname": 'Jeffie',
#         "Lastname": 'Abadam',
#         "Pronouns": 'he/him',
#         "Date of Birth": '23/28/2003',
#         "occupation": 'VP Product Management',
#         "Account Balance": '-682162471',
#         "Overdraft Limit": '614776292'
#     }
#     assert_dict_equal(expected, x.to_dict(), "the wrong client was outputted")
#
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














