import pandas as pd


class client_class:
    #constructor
    def __init__(self,title,first_name,last_name,preferred_pronouns,date_of_birth,occupation,account_balance,overdraft_limit):
        #instance variables
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.title = str(title)
        self.preferred_pronouns = str(preferred_pronouns)
        self.date_of_birth = str(date_of_birth)
        self.occupation = str(occupation)
        self.account_balance = int(account_balance)
        self.overdraft_limit = int(overdraft_limit)

    def __str__(self):
         return (
             f'Title: {self.title}\n'
             f'Firstname: {self.first_name}\n'
             f'Lastname: {self.last_name}\n'
             f'Preferred Pronoun: {self.preferred_pronouns}\n'
             f'Date of Birth: {self.date_of_birth}\n'
             f'Occupation: {self.occupation}\n'
             f'Account Balance: £{self.account_balance}\n'
             f'Overdraft Limit: £{self.overdraft_limit}')

    def __repr__(self):
        return (
            f"{self.title},{self.first_name},{self.last_name},{self.preferred_pronouns},{self.date_of_birth},{self.occupation},{self.account_balance},{self.overdraft_limit}")

    def adding_in_account_balance(self,add_balance):
        new_balance =  int(add_balance) + int(self.account_balance)
        self.account_balance=new_balance


    def removing_in_account_balance(self,removing_balance):
        if removing_balance > (self.account_balance + self.overdraft_limit):
            self.account_balance = (self.account_balance + self.overdraft_limit) - (removing_balance + 5)
        else:
            self.account_balance = (self.account_balance - removing_balance)

    def changing_title(self,new_title):
        self.title = new_title

    def changing_first_name(self,new_first_name):
        self.first_name = new_first_name
    def changing_last_name(self,new_last_name):
        self.last_name = new_last_name
    def changing_preferred_pronoun(self,new_preferred_pronoun):
        self.preferred_pronouns=new_preferred_pronoun

    def changing_occupation(self,new_occupation):
        self.occupation = new_occupation

    def return_client_dict(self):
        return {
        "Title": [f"{self.title}"],
        "Firstname": [f"{self.first_name}"],
        "Lastname": [f"{self.last_name}"],
        "Pronouns": [f"{self.preferred_pronouns}"],
        "Date of Birth": [f"{self.date_of_birth}"],
        "Occupation": [f"{self.occupation}"],
        "Account Balance": [self.account_balance],
        "Overdraft Limit": [self.overdraft_limit]
    }


