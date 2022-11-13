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
        dataframe = csv_class_obj.dataframe_of_csv_file()
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
        dataframe.drop(dataframe[(dataframe["Firstname"] == first_name) & (dataframe["Lastname"] == last_name) & (dataframe["Date of Birth"] == date_of_birth)].index, inplace=True)
        self.csv_class_obj.refresh_csv_file(dataframe)

    def changing_overdraft_limits(self,first_name, last_name, date_of_birth, new_overdraft_limit):
        dataframe = self.__fetch_csv_dataframe()
        for index, row in dataframe.iterrows():
            if row['Firstname'] == first_name and row['Lastname'] == last_name and row['Date of Birth'] == date_of_birth:
                dataframe.at[index, 'Overdraft Limit'] = new_overdraft_limit
        self.csv_class_obj.refresh_csv_file(dataframe)

    def print_current_CSV_file(self):
        print(self.__fetch_csv_dataframe().to_string())

    def adding_a_client(self,title,first_name,last_name,pronouns,DoB,occupation,account_balance, overdraft_limit):
        dataframe = self.__fetch_csv_dataframe()
        self.csv_class_obj.refresh_csv_file(dataframe)

#Objects of each class
BA_Obj = Banking_Application()
csv_obj = csv()
client_obj = client_class()






# retrieved_client_obj = BA_Obj.retrieving_a_client("Skyler","Harrinson", "2/23/1960")
# print(retrieved_client_obj)

#BA_Obj.deleting_a_client("Wilma","Huniwall","4/14/2000"
# BA_Obj.changing_overdraft_limits("Skyler","Harrinson", "2/23/1960",1000)
# BA_Obj.print_current_CSV_file()


#printing all accounts with negative balance
# print(BA_Obj.accounts_with_negative_balance())


# #printing the csv file

print(csv_obj.add_to_csv_file(c))
#
#

# csv.add_to_csv_file(c)
