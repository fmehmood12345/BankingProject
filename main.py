# #One Client
import pandas as pd
from banking_application import Banking_Application
from clients import client_class




BA_Obj = Banking_Application()

client = {
        "title": 'Mr',
        "first_name": 'Farheen',
        "last_name": 'Smith',
        "preferred_pronouns": 'he/him',
        "date_of_birth": '15/12/1990',
        "occupation": 'Software Engineer',
        "account_balance": 100,
        "overdraft_limit": 10
    }
client_object = client_class(**client)

print(BA_Obj.accounts_with_negative_balance())
print(" ")
BA_Obj.deleting_a_client("Alice","Liddyard","8/31/1978")
BA_Obj.changing_overdraft_limits("Skyler","Harrinson","2/23/1960","156")
BA_Obj.adding_a_client(client_object.return_client_dict())
print(BA_Obj.print_current_CSV_file())




#print(BA_Obj.retrieving_a_client("Wilma","Huniwall","4/14/2000"))




























