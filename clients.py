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

    def adding_in_account_balance(self,add_balance):
        old_account_balance = self.account_balance
        new_balance =  int(add_balance) + int(old_account_balance)
        return  new_balance

    def removing_in_account_balance(self,removing_balance):
        old_account_balance = self.account_balance
        new_balance =  int(old_account_balance)-int(removing_balance)
        if removing_balance > int(self.overdraft_limit):
            new_balance = int(old_account_balance) - (int(removing_balance)+5)
        return new_balance

    def

client = {
        "title": "Mr",
        "first_name" : "Mike",
        "last_name": "Smith",
        "preferred_pronouns": "he/him",
        "date_of_birth": "15/12/1990",
        "occupation": "Software Engineer",
        "account_balance": "100",
        "overdraft_limit": "10"
    }
#Adding client into the attributes in client_details class
c = client_details(**client)

#Adding balance
c.account_balance=(c.adding_in_account_balance(add_balance=100))
print(c.account_balance)

#removing balance
c.account_balance=(c.removing_in_account_balance(removing_balance=11))
print(c.account_balance)
