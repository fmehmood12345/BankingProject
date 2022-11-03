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
        if removing_balance > (int(old_account_balance)+ int(self.overdraft_limit)):
            new_balance = -5 # HAVE TO CHECK
        return new_balance

    def changing_title(self,new_title):
        old_title = self.title
        updated_title=new_title
        return updated_title

    def changing_first_name(self,new_first_name):
        old_first_name = self.first_name
        updated_first_name = new_first_name
        return updated_first_name
    def changing_last_name(self,new_last_name):
        old_last_name = self.last_name
        updated_last_name = new_last_name
        return updated_last_name

    def changing_preferred_pronoun(self,new_preferred_pronoun):
        old_preferred_pronoun = self.preferred_pronouns
        updated_preferred_pronoun = new_preferred_pronoun
        return updated_preferred_pronoun

    def changing_occupation(self,new_occupation):
        old_occupation = self.occupation
        updated_occupation = new_occupation
        return updated_occupation

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

#Client before changes made
print(c)

#Adding balance
c.account_balance=(c.adding_in_account_balance(add_balance=100))
print(c.account_balance)

#removing balance
c.account_balance=(c.removing_in_account_balance(removing_balance=1100))
print(c.account_balance)

#changing the title
c.title=(c.changing_title("Mrs"))
print(c.title)

#changing the firstname
c.first_name=(c.changing_first_name("Sarah"))
print(c.first_name)

c.last_name=(c.changing_last_name("Dott"))
print(c.last_name)

c.preferred_pronouns=(c.changing_preferred_pronoun("she/her"))
print(c.preferred_pronouns)

c.occupation=(c.changing_occupation("Teacher"))
print(c.occupation)

#Check to see if the dictionary is actually updated
print(c)
