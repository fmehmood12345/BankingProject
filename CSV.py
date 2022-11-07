import csv
import pandas as pd

class csv:
    def dictionary_of_csv_file():
        df = pd.read_csv('./database/clients_details.csv')
        return (df.to_string())
    def add_to_csv_file(self):
        df.to_csv('./database/clients_details.csv', mode='a', index=False, header=False)

        '''new_client we will get from the banking application class - to make a new client we will add all its information into this variable and
        pass it as an argument.'''


print(csv.dictionary_of_csv_file())