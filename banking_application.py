from clients import *
from CSV import *
import datetime
import pandas as pd

'''What to have in the banking application class:
            -retrieving a client by searching first and last name and DoB
            -Change overdraft limits once you have retrieved a client
            -Add and Delete clients
            -Search by negative balance
            -move money from one account to another    '''

class Banking_Application:

    def __fetch_csv_dataframe(self):
        csv_class_obj = csv()
        dataframe = csv_class_obj.dictionary_of_csv_file()
        return dataframe

    def __return_client_df_as_dict(self, dataframe_input):
        client_dict = {
            "title": dataframe_input['Title'].loc[dataframe_input.index[0]],
            "first_name": dataframe_input['Firstname'].loc[dataframe_input.index[0]],
            "last_name": dataframe_input['Lastname'].loc[dataframe_input.index[0]],
            "preferred_pronouns": dataframe_input['Pronouns'].loc[dataframe_input.index[0]],
            "date_of_birth": dataframe_input['Date of Birth'].loc[dataframe_input.index[0]],
            "occupation": dataframe_input['Occupation'].loc[dataframe_input.index[0]],
            "account_balance": dataframe_input['Account Balance'].loc[dataframe_input.index[0]],
            "overdraft_limit": dataframe_input['Overdraft Limit'].loc[dataframe_input.index[0]]
        }
        return client_dict

    def retrieving_a_client(self, first_name,last_name,date_of_birth):
        dataframe = self.__fetch_csv_dataframe()
        df = dataframe[
            (dataframe["Firstname"] == first_name) &
            (dataframe["Lastname"] == last_name) &
            (dataframe["Date of Birth"] == date_of_birth)
            ]
        client_obj = client_class(**self.__return_client_df_as_dict(df))
        return client_obj


    def accounts_with_negative_balance(self):
        dataframe = self.__fetch_csv_dataframe()
        df = dataframe[dataframe["Account Balance"] < 0]
        return df.to_string()

    def deleting_a_client(self,first_name, last_name, date_of_birth):
        dataframe = self.__fetch_csv_dataframe()
        dataframe.drop(dataframe.index[(dataframe["Firstname"] == first_name)],axis=0,inplace=True)
        return dataframe.to_string()

    # def changing_overdraft_limits():
    #     return None


    # def moving_money_between_clients():
    #     return None



BA_Obj = Banking_Application()

retrieved_client_obj = BA_Obj.retrieving_a_client("Skyler","Harrinson", "2/23/1960")
#print(retrieved_client_obj)

deleting_a_client_obj = BA_Obj.deleting_a_client("Lorant","Sphinxe","1/29/1971")

# #printing all accounts with negative balance
#print(BA_Obj.accounts_with_negative_balance())


# #printing the csv file
# print(csv.dictionary_of_csv_file())
#
#

