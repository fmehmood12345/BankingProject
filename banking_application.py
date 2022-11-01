import csv
import database
import  clients

#class for banking application
class Banking_Application:

    def __init__(self):
        with open("database/clients_details.csv","r") as x:
            reader = csv.reader(x)
            for i in reader:
                print(i)




#appending client details to csv file
filename = 'clients_details.csv'
with open(filename, 'a') as file_object:
    client1 = clients.client_details('Ms', 'Skyler', 'Harrinson', 'they', '2/23/1960', 'Research and Development',
                                     '4562', '100')
    file_object.write(client1.__str__())

with open('database/clients_details.csv') as file_object:
    content = file_object.read()
print(content)




