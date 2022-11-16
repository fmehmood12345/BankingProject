from clients import *
from CSV import *
import pandas as pd
from constants import *

'''Functions in the banking application class:
            -Fetching the CSV dataframe
            -Printing the CSV dataframe
            -Private function which returns the client dataframe as a dictionary
            -Retrieving a client by searching first and last name and DoB
            -Change overdraft limits once you have retrieved a client
            -Add clients
            -Delete clients
            -Search by firstname
            -Search by lastname
            -Search by date of birth
            -Search by negative balance   '''


class Banking_Application:

    def __init__(self):
        self.csv_class_obj = csv()

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

    def retrieving_a_client(self, first_name, last_name, date_of_birth):
        dataframe = self.__fetch_csv_dataframe()
        if (first_name == dataframe["Firstname"].to_string()) and (last_name == dataframe["Lastname"].to_string()) and (date_of_birth == dataframe["Date of Birth"].to_string()):
            df = dataframe[
                (dataframe.Firstname == first_name) &
                (dataframe.Lastname == last_name) &
                (dataframe["Date of Birth"] == date_of_birth)
                ]
            print(df.loc[95])
            client_obj = client_class(**self.__return_client_df_as_dict(**(df.loc[95].to_dict())))
            return client_obj
        else:
            print("Error: There is no client called", first_name, last_name, "with date of birth", date_of_birth,
                  "in the CSV file.")

    def searching_for_accounts_with_negative_balance(self):
        dataframe = self.__fetch_csv_dataframe()
        df = dataframe[dataframe["Account Balance"] < 0]
        return df.to_dict()

    def searching_by_firstname(self, first_name):
        # if first_name == dataframe["Firstname"].to_string():
        dataframe = self.__fetch_csv_dataframe()
        df = dataframe[(dataframe["Firstname"] == first_name)]
        return df.to_dict()
        # else:
        #     print("Error: There is no one with the firstname: ",first_name)

    def searching_by_lastname(self, last_name):
        # if last_name == dataframe["Lastname"].to_string():
        dataframe = self.__fetch_csv_dataframe()
        df = dataframe[(dataframe["Lastname"] == last_name)]
        return df.to_dict()
        # else:
        #     print("Error: There is no one with the lastname: ",last_name)


    def searching_by_date_of_birth(self, date_of_birth):
        dataframe = self.__fetch_csv_dataframe()
        #if date_of_birth == dataframe["Date of Birth"].to_string():
        df = dataframe[(dataframe["Date of Birth"] == date_of_birth)]
        return df.to_dict()
        # else:
        #     print("Error: There is no one with date of birth: ",date_of_birth)

    def deleting_a_client(self, first_name, last_name, date_of_birth):
        dataframe = self.__fetch_csv_dataframe()
        #if (first_name == dataframe["Firstname"].to_string()) and (last_name == dataframe["Lastname"].to_string()) and (date_of_birth == dataframe["Date of Birth"].to_string()):
        dataframe.drop(dataframe[(dataframe["Firstname"] == first_name) & (dataframe["Lastname"] == last_name) & (dataframe["Date of Birth"] == date_of_birth)].index, inplace=True)
        self.csv_class_obj.refresh_csv_file(dataframe)
        # else:
        #     print("Error: There is no client called", first_name, last_name, "with date of birth", date_of_birth,
        #           "in the CSV file.")

    def adding_a_client(self, client_dict):
        dataframe = self.__fetch_csv_dataframe()
        client_dataframe = pd.DataFrame(client_dict)
        #if client_dataframe["Firstname"].to_string() != dataframe["Firstname"].to_string() and (client_dataframe["Lastname"].to_string() == dataframe["Lastname"].to_string()) and (client_dataframe["Date of Birth"].to_string() == dataframe["Date of Birth"].to_string()):
        new_dataframe = pd.concat([dataframe, client_dataframe], ignore_index=True)
        self.csv_class_obj.refresh_csv_file(new_dataframe)
        # else:
        #     print("Error: There is already a client called", client_dataframe["first_name"].to_string(),
        #           client_dataframe["last_name"].to_string(), "with date of birth",
        #           client_dataframe["date_of_birth"].to_string())

    def changing_overdraft_limits(self, first_name, last_name, date_of_birth, new_overdraft_limit):
        dataframe = self.__fetch_csv_dataframe()
        #if (first_name == dataframe["Firstname"].to_string()) and (last_name == dataframe["Lastname"].to_string()) and (date_of_birth == dataframe["Date of Birth"].to_string()):
        for index, row in dataframe.iterrows():
            if row['Firstname'] == first_name and row['Lastname'] == last_name and row['Date of Birth'] == date_of_birth:
                dataframe.at[index, 'Overdraft Limit'] = new_overdraft_limit
                self.csv_class_obj.refresh_csv_file(dataframe)
        # else:
        #     print("Error: There is no client called", first_name, last_name, "with date of birth", date_of_birth,
        #           "in the CSV file. Overdraft limit cannot be changed.")
