import pandas as pd
from banking_application import Banking_Application
from clients import client_class

client = {
        "title": 'Mr',
        "first_name": "Henry",
        "last_name": 'Smith',
        "preferred_pronouns": 'he/him',
        "date_of_birth": '15/12/1990',
        "occupation": 'Software Engineer',
        "account_balance": 100,
        "overdraft_limit": 10
    }
client_object = client_class(**client)
BA_Obj = Banking_Application()


# client_object.changing_title("Mrs")
# client_object.changing_first_name("Susan")
# client_object.changing_last_name("Blunt")
# client_object.changing_preferred_pronoun("she/her")
# client_object.changing_occupation("Designer")
# client_object.removing_in_account_balance(100)
# client_object.adding_in_account_balance(200)
# print(client_object.return_client_dict())


# #How to change the details of a client once it has been received:
# client_from_CSV_File = BA_Obj.retrieving_a_client("Gerald", "Smith", "15/12/1990")
# client_object_1 = client_class(**client_from_CSV_File)
# client_object_1.changing_title("Mrs")
# client_object_1.changing_first_name("Susan")
# client_object_1.changing_last_name("Blunt")
# client_object_1.changing_preferred_pronoun("she/her")
# client_object_1.changing_occupation("Designer")
# client_object_1.removing_in_account_balance(100)
# client_object_1.adding_in_account_balance(200)
# print(client_object.return_client_dict())


#BA_Obj.deleting_a_client("Alice","Liddyard","8/09/1978")
BA_Obj.changing_overdraft_limits("Skyler","Harrinson","2/07/1960",1517)
#BA_Obj.adding_a_client(client_object.return_client_dict())

#print(BA_Obj.searching_for_accounts_with_negative_balance())
# print(BA_Obj.print_current_CSV_file())
#print(BA_Obj.retrieving_a_client("Gerald", "Smith", "15/12/1990"))
#print(BA_Obj.searching_by_firstname("Wilma"))
#print(BA_Obj.searching_by_lastname("Huniwall"))
#print(BA_Obj.searching_by_date_of_birth("10/04/1979"))


