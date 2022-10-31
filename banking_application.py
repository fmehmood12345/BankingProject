import csv
import database
import  clients

class Banking_Application:

    def __init__(self):
        with open("database/clients_details.csv","r") as x:
            reader = csv.reader(x)
            for i in reader:
                print(i)

bank = Banking_Application()

client1= clients.client_details('Ms', 'Skyler', 'Harrinson', 'they', '2/23/1960', 'Research and Development', '5945', '100')
print(client1.first_name)



