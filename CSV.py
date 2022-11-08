import csv

import pandas
import pandas as pd


class csv:

    def dictionary_of_csv_file():
        dataframe = pd.read_csv('./database/clients_details.csv')
        return (dataframe.to_string())

    def add_to_csv_file(client):
        df = pd.DataFrame(client)
        df.to_csv('./database/clients_details.csv', mode='a', index=False, header=False)

