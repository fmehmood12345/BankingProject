import csv
import datetime
import pandas
import pandas as pd
from constants import *


class csv:

    def dataframe_of_csv_file(self):
        dataframe = pd.read_csv(CSV_FILE_PATH)
        return dataframe

    def refresh_csv_file(self, new_df):
        current_df = pd.read_csv(CSV_FILE_PATH)
        current_df = new_df
        current_df.to_csv(CSV_FILE_PATH)


    def add_to_csv_file(self, client):
        df = pd.DataFrame(client)
        df.to_csv(CSV_FILE_PATH, mode='a', index=False, header=False)

csv_class_obj = csv()

