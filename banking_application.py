from clients import *
from CSV import *
import datetime
import pandas as pd
from constants import *

'''What to have in the banking application class:
            -retrieving a client by searching first and last name and DoB
            -Change overdraft limits once you have retrieved a client
            -Add and Delete clients
            -Search by negative balance
            -move money from one account to another    '''

class Banking_Application:

    def __init__(self):
        self.csv_class_obj= csv()

    def __fetch_csv_dataframe(self):
        dataframe = self.csv_class_obj.dataframe_of_csv_file()
        return dataframe

    def print_current_CSV_file(self):
        print(self.__fetch_csv_dataframe().to_string())

    def __return_client_df_as_dict(self, **dataframe_input):
        client_dict = {
            "title": dataframe_input['Title'],
            "first_name": dataframe_input['Firstname'],
            "last_name": dataframe_input['Lastname'],
            "preferred_pronouns": dataframe_input['Pronouns'],
            "date_of_birth": dataframe_input['Date of Birth'],
            "occupation": dataframe_input['Occupation'],
            "account_balance": dataframe_input['Account Balance'],
            "overdraft_limit": dataframe_input['Overdraft Limit']
        }
        return client_dict

    def retrieving_a_client(self, first_name,last_name,date_of_birth):
        dataframe = self.__fetch_csv_dataframe()

        df = dataframe[
            (dataframe.Firstname == first_name) &
            (dataframe.Lastname == last_name) &
            (dataframe["Date of Birth"] == date_of_birth)
            ]
        print(df.loc[95])

        client_obj = client_class(**self.__return_client_df_as_dict(**(df.loc[95].to_dict())))
        return client_obj


    def accounts_with_negative_balance(self):
        dataframe = self.__fetch_csv_dataframe()
        df = dataframe[dataframe["Account Balance"] < 0]
        return df.to_string()

    def deleting_a_client(self,first_name, last_name, date_of_birth):
        dataframe = self.__fetch_csv_dataframe()
        dataframe.drop(dataframe[(dataframe["Firstname"] == first_name) & (dataframe["Lastname"] == last_name) & (dataframe["Date of Birth"] == date_of_birth)].index, inplace=True)
        self.csv_class_obj.refresh_csv_file(dataframe)

    def changing_overdraft_limits(self,first_name, last_name, date_of_birth, new_overdraft_limit):
        dataframe = self.__fetch_csv_dataframe()
        for index, row in dataframe.iterrows():
            if row['Firstname'] == first_name and row['Lastname'] == last_name and row['Date of Birth'] == date_of_birth:
                dataframe.at[index, 'Overdraft Limit'] = new_overdraft_limit
        self.csv_class_obj.refresh_csv_file(dataframe)

    def adding_a_client(self, client_dict):
        dataframe = self.__fetch_csv_dataframe()
        client_dataframe = pd.DataFrame(client_dict)
        new_dataframe = pd.concat([dataframe, client_dataframe], ignore_index=True)
        self.csv_class_obj.refresh_csv_file(new_dataframe)

