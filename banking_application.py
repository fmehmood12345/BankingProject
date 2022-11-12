from clients import *
from CSV import *
import datetime
'''What to have in the banking application class:
            -retrieveing a client by searching first and last name and DoB
            -Change overdraft limits once you have retrieved a client
            -Add and Delete clients
            -Search by negative balance
            -move money from one account to another    '''

class Banking_Application:

    def __fetch_csv_dataframe(self):
        csv_class_obj = csv()
        dataframe = csv.dictionary_of_csv_file()
        return dataframe
    def retrieving_a_client(self, first_name,last_name,date_of_birth):
        dataframe = self.__fetch_csv_dataframe()
        df = dataframe[(dataframe["Firstname"] == first_name) & (dataframe["Lastname"] == last_name) & (dataframe["Date of Birth"] == date_of_birth)]
        return df.to_string()
    def accounts_with_negative_balance(self):
        dataframe = self.__fetch_csv_dataframe()
        df = dataframe[dataframe["Account Balance"] < 0]
        return (df.to_string())
    def deleting_a_client():
        return None
    def changing_overdraft_limits():
        return None
    def moving_money():
        return None



BA_Obj = Banking_Application()

print(BA_Obj.retrieving_a_client("Skyler","Harrison", "2/23/1960"))

# #printing all accounts with negative balance
# print(Banking_Application.accounts_with_negative_balance(df))
#
#
# #adding client to csv file
# csv.add_to_csv_file(client)
#
# #printing the csv file
# print(csv.dictionary_of_csv_file())
#
#

