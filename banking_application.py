from clients import *
from CSV import *
import pandas as pd
from constants import *

class Banking_Application:

    def __init__(self):
        self.csv_class_obj = csv()
    '''Made a constructor which is an object of the CSV class so that I can assess the functions in that class. '''

    def __fetch_csv_dataframe(self):
        dataframe = self.csv_class_obj.dataframe_of_csv_file()
        return dataframe
    '''Private method which uses an object of the CSV class to call the function "dataframe_of_csv_file()" to get the 
    CSV file as dataframe.'''

    def print_current_CSV_file(self):
        print(self.__fetch_csv_dataframe().to_string())
    '''Method to print out the dataframe by running the private method.'''

    def __return_client_df_as_dict(self, **dataframe_input):
        client_dict = {
            "title": list(dataframe_input["Title"].values())[0],
            "first_name": list(dataframe_input["Firstname"].values())[0],
            "last_name": list(dataframe_input["Lastname"].values())[0],
            "preferred_pronouns": list(dataframe_input["Pronouns"].values())[0],
            "date_of_birth": list(dataframe_input["Date of Birth"].values())[0],
            "occupation": list(dataframe_input["Occupation"].values())[0],
            "account_balance": list(dataframe_input["Account Balance"].values())[0],
            "overdraft_limit": list(dataframe_input["Overdraft Limit"].values())[0]
        }
        return client_dict
    '''Private method to return a client which is a dataframe as a dictionary. This is so that clients are presented in a cleaner way as opposed to a dictionary. 
    In this method, the dataframe of the client is inputted as an attribute and returns the client in a cleaner form.'''

    def retrieving_a_client(self, first_name, last_name, date_of_birth):
        dataframe = self.__fetch_csv_dataframe()
        #if (first_name == dataframe["Firstname"].to_string()) and (last_name == dataframe["Lastname"].to_string()) and (date_of_birth == dataframe["Date of Birth"].to_string()):
        df = dataframe[
            (dataframe.Firstname == first_name) &
            (dataframe.Lastname == last_name) &
            (dataframe["Date of Birth"] == date_of_birth)
            ]
        client_obj = client_class(**self.__return_client_df_as_dict(**(df.to_dict())))
        return client_obj
        #else:
            # print("Error: There is no client called", first_name, last_name, "with date of birth", date_of_birth,
            #       "in the CSV file.")
    '''This method retrieves a client from the CSV dataframe by calling the private function. Then the firstname, 
    lastname and date of birth called into the function is compared with the firstname, lastname and date of birth in 
    the CSV dataframe to find the respective client. Once they have been found, they are put in a dataframe. Then this
    client dataframe is called into a function which returns a client as a dictionary. Finally this dictionary is 
    returned.'''

    def searching_for_accounts_with_negative_balance(self):
        dataframe = self.__fetch_csv_dataframe()
        df = dataframe[dataframe["Account Balance"] < 0]
        return df.to_string()
    '''This method get returns all clients with negative balance as a dataframe as there are multiple clients 
    that could be returned. It fetches the CSV dataframe and gets all clients with negative account balance. '''

    def searching_by_firstname(self, first_name):
        # if first_name == dataframe["Firstname"].to_string():
        dataframe = self.__fetch_csv_dataframe()
        df = dataframe[(dataframe["Firstname"] == first_name)]
        return df.to_string()
        # else:
        #     print("Error: There is no one with the firstname: ",first_name)
    ''' This method compares the firstname passed in the parameter with all the available first names and returns all
    details of the clients as a dataframe.'''

    def searching_by_lastname(self, last_name):
        # if last_name == dataframe["Lastname"].to_string():
        dataframe = self.__fetch_csv_dataframe()
        df = dataframe[(dataframe["Lastname"] == last_name)]
        client_obj = client_class(**self.__return_client_df_as_dict(**(df.to_dict())))
        return client_obj
        # else:
        #     print("Error: There is no one with the lastname: ",last_name)
    ''' '''

    def searching_by_date_of_birth(self, date_of_birth):
        dataframe = self.__fetch_csv_dataframe()
        #if date_of_birth == dataframe["Date of Birth"].to_string():
        df = dataframe[(dataframe["Date of Birth"] == date_of_birth)]
        client_obj = client_class(**self.__return_client_df_as_dict(**(df.to_dict())))
        return client_obj
        # else:
        #     print("Error: There is no one with date of birth: ",date_of_birth)
    ''' '''

    def deleting_a_client(self, first_name, last_name, date_of_birth):
        dataframe = self.__fetch_csv_dataframe()
        #if (first_name == dataframe["Firstname"].to_string()) and (last_name == dataframe["Lastname"].to_string()) and (date_of_birth == dataframe["Date of Birth"].to_string()):
        dataframe.drop(dataframe[(dataframe["Firstname"] == first_name) & (dataframe["Lastname"] == last_name) & (dataframe["Date of Birth"] == date_of_birth)].index, inplace=True)
        self.csv_class_obj.refresh_csv_file(dataframe)
        # else:
        #     print("Error: There is no client called", first_name, last_name, "with date of birth", date_of_birth,
        #           "in the CSV file.")
    ''' '''

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
    ''' '''

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
    ''' '''