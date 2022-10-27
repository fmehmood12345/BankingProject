import csv
from pythonAssessment2 import database
import client_details

class Banking_Application:

    def __init__(self):
        with open("database/clients_details.csv","r") as x:
            reader = csv.reader(x)
            for i in reader:
                print(i)
bank = Banking_Application()

reader = client_details.reader(x)
for i in reader:
    print(i)

