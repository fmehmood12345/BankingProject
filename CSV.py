import csv
import datetime
import pandas
import pandas as pd


class csv:

    def dictionary_of_csv_file(self):
        dataframe = pd.read_csv('./database/clients_details.csv')
        return dataframe

    def changing_datatypes(self):
        dataframe = self.dictionary_of_csv_file()

        # title = list(dataframe['Title'])
        # title_string = ' '.join(str(i) for i in title)
        #
        # firstname = list(dataframe['Firstname'])
        # firstname_string = ' '.join(str(i) for i in firstname)
        #
        # lastname = list(dataframe['Lastname'])
        # lastname_string = ' '.join(str(i) for i in lastname)
        #
        # pronouns = list(dataframe['Pronouns'])
        # pronouns_string = ' '.join(str(i) for i in pronouns)

        # date_of_birth = list(dataframe["Date of Birth"])
        # date_of_birth_string = ' '.join(datetime(i) for i in date_of_birth)

        # occupation = list(dataframe['Occupation'])
        # occupation_string = ' '.join(str(i) for i in occupation)

        dataframe['Account Balance'] = pd.to_numeric(dataframe['Account Balance'], errors="coerce").fillna(0).astype(int).to_frame()
        dataframe['Title'] = dataframe['Title'].astype(str)
        #dataframe['Date of Birth'] = pd.to_datetime(['Date of Birth'], errors="coerce")
        print(dataframe.dtypes)
    def add_to_csv_file(client):
        df = pd.DataFrame(client)
        df.to_csv('./database/clients_details.csv', mode='a', index=False, header=False)

csv_class_obj = csv()
