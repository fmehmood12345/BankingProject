import csv

import pandas
import pandas as pd


class csv:
    # def __init__(self,df):
    #     self.df = df
    def dictionary_of_csv_file(dataframe):
        dataframe = pd.read_csv('./database/clients_details.csv')
        return (dataframe.to_string())

    # def add_to_csv_file(new_client):
    #     #df = pd.read_csv('./database/clients_details.csv')
    #     df=pandas.DataFrame(new_client)
    #     with open('./database/clients_details.csv', 'a') as f:
    #         df.to_csv(f, header=f.tell()==0) # puts df in the CSV file but I cant figure out how to put the client
    #     # df.to_csv('./database/clients_details.csv', mode='a', index=False, header=False)
    #
    #     '''new_client we will get from the banking application class - to make a new client we will add all its information into this variable and
    #     pass it as an argument.'''

    def add_to_dataframe(dataframe,new_client):
        length = len(dataframe)
        dataframe.loc[length] = new_client
        return (dataframe.to_string())

#print(csv.add_to_csv_file())
#print(csv.dictionary_of_csv_file())