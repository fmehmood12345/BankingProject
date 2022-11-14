import csv
import datetime
import pandas
import pandas as pd
from constants import *


class csv:
   # , index_col = "Title"
    def dataframe_of_csv_file(self):
        dataframe = pd.read_csv(CSV_FILE_PATH, index_col="Title")
        return dataframe

    def refresh_csv_file(self, new_df):
        with open(CSV_FILE_PATH, 'w') as my_new_csv_file:
            new_df.to_csv(CSV_FILE_PATH, mode="w", index="False")
            my_new_csv_file.close()

csv_class_obj = csv()
