#Class for client_details
class client_details:

    #constructor
    def __init__(self,title,first_name,last_name,preferred_pronouns,date_of_birth,occupation,account_balance,overdraft_limit):
        #instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.preferred_pronouns = preferred_pronouns
        self.date_of_birth = date_of_birth
        self.occupation = occupation
        self.account_balance = account_balance
        self.overdraft_limit = overdraft_limit

    # #method explaining how data should be ordered
    # def order(self):
    #     return (
    #         f"{self.title},{self.first_name},{self.last_name},{self.preferred_pronouns},{self.date_of_birth},{self.occupation},{self.account_balance},{self.overdraft_limit}")
    #
    def __str__(self):
         return (
             f'{self.title},{self.first_name},{self.last_name},{self.preferred_pronouns},{self.date_of_birth},{self.occupation},{self.account_balance},{self.overdraft_limit}')

    def __repr__(self):
        return (
            f"{self.title},{self.first_name},{self.last_name},{self.preferred_pronouns},{self.date_of_birth},{self.occupation},{self.account_balance},{self.overdraft_limit}")

    def changing_account_balance(self,new_account_balance):
        old_account_balance = self.account_balance
        new_balance =  int(new_account_balance) + int(old_account_balance)
        return  new_balance


client = {
        "title": "Mr",
        "first_name" : "Mike",
        "last_name": "Smith",
        "preferred_pronouns": "he/him",
        "date_of_birth": "15/12/1990",
        "occupation": "Software Engineer",
        "account_balance": "158972",
        "overdraft_limit": "1000"
    }
#Adding client into the attributes in client_details class
c = client_details(**client)

c.account_balance=(c.changing_account_balance(new_account_balance=100))
print(c.account_balance)

