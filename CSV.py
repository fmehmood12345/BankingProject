import csv
import datetime
import pandas
import pandas as pd
from constants import *


class csv:
    def dataframe_of_csv_file(self):
        dataframe = pd.read_csv(CSV_FILE_PATH, index_col=None)
        return dataframe
    '''The method takes the client details and turns it into a dataframe.'''
    def refresh_csv_file(self, new_df):
        new_df.to_csv(CSV_FILE_PATH, index=False)
    '''This method takes in the updated dataframe once the changes have been made and refreshes the CSV file. '''
