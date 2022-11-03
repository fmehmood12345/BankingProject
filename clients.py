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

    def changing_title(self,title, first_name, last_name):

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
c = client_details(**client)
print(c)