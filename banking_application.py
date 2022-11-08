from clients import *
from CSV import *

#reading from the csv file and putting it into a df format
df = pd.read_csv('./database/clients_details.csv')
#adding client to csv file
csv.add_to_csv_file(client)
#printing the csv file
print(csv.dictionary_of_csv_file())





#class for banking application
# class Banking_Application:
#     def __init__(self):
#         with open("database/clients_details.csv","r") as x:
#             reader = csv.reader(x)
#             for i in reader:
#                 print(i)
#
# filename = 'database/clients_details.csv'
#
# #Adding Clients: appending client details to csv file
# with open(filename, 'a',newline='') as file_object:
#     writer_object = writer(file_object)
#     client1 = clients.client_details('Ms', 'Skyler', 'Harrinson', 'they', '2/23/1960', 'Research and Development',
#                                      '4562', '100')
#     client1_list = []
#     for value in client1.__str__().split(','):
#         client1_list.append(value)
#     writer_object.writerow(client1_list)
#
# file_object.close()
#
# #Proof of Adding Clients
# with open(filename) as file_object:
#      content = file_object.read()
# print(content)
#
# #Deleting Cliets from CSV file
# lines = list()
# client_name = input("Enter the firstname of the client you want to delete ")
# with open(filename, 'r') as readFile:
#     reader = csv.reader(readFile)
#     for row in reader:
#         lines.append(row)
#         for field in row:
#             if field == client_name:
#                 lines.remove(row)
#     for i in lines:
#         print(i)
#
# #Writing the CSV file into a list
# with open(filename, 'w') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(lines)
# # print(lines)
#



