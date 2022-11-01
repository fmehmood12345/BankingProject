import csv
import database
import  clients
from csv import writer

#class for banking application
class Banking_Application:

    def __init__(self):
        with open("database/clients_details.csv","r") as x:
            reader = csv.reader(x)
            for i in reader:
                print(i)




#Adding Clients: appending client details to csv file
filename = 'database/clients_details.csv'

with open(filename, 'a',newline='') as file_object:
    writer_object = writer(file_object)
    client1 = clients.client_details('Ms', 'Skyler', 'Harrinson', 'they', '2/23/1960', 'Research and Development',
                                     '4562', '100')
    client1_list = []
    for value in client1.__str__().split(','):
        client1_list.append(value)
    writer_object.writerow(client1_list)

file_object.close()

#Proof of Adding Clients5
with open('database/clients_details.csv') as file_object:
    content = file_object.read()
print(content)




