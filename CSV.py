import csv
import pandas as pd

class CSV:

    def dictionary_of_csv_file():
        df = pd.read_csv('./database/clients_details.csv')
        records = df.to_dict(orient='records')
        for row in records:
            print(row)

    def add_to_csv_file(self,new_client):
        pd.to_csv("new_client")

        '''new_client we will get from the banking application class - to make a new client we will add all its information into this variable and
        pass it as an argument'''

CSV.dictionary_of_csv_file()