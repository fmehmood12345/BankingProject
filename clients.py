import pandas as pd


class client_class:
    # constructor
    def __init__(self, title, first_name, last_name, preferred_pronouns, date_of_birth, occupation, account_balance,
                 overdraft_limit):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.preferred_pronouns = preferred_pronouns
        self.date_of_birth = date_of_birth
        self.occupation = occupation
        self.account_balance = account_balance
        self.overdraft_limit = overdraft_limit
    '''Client class constructor with all the class attributes needed for each client.'''
    def __str__(self):
        return (
            f'Title: {self.title}\n'
            f'Firstname: {self.first_name}\n'
            f'Lastname: {self.last_name}\n'
            f'Preferred Pronoun: {self.preferred_pronouns}\n'
            f'Date of Birth: {self.date_of_birth}\n'
            f'Occupation: {self.occupation}\n'
            f'Account Balance: {self.account_balance}\n'
            f'Overdraft Limit: {self.overdraft_limit}')
    '''An str method which presents the client data in a specific way '''
    # def __repr__(self):
    #     return (
    #         f"{self.title},{self.first_name},{self.last_name},{self.preferred_pronouns},{self.date_of_birth},{self.occupation},{self.account_balance},{self.overdraft_limit}")

    def adding_in_account_balance(self, add_balance):
        new_balance = int(add_balance) + int(self.account_balance)
        self.account_balance = new_balance
    '''This method deposits money into the clients account balance'''
    def removing_in_account_balance(self, removing_balance):
        if removing_balance > (self.account_balance + self.overdraft_limit):
            self.account_balance = (self.account_balance + self.overdraft_limit) - (removing_balance + 5)
        else:
            self.account_balance = (self.account_balance - removing_balance)
    '''This method withdraws money from the account balance and if the overdraft limit is surpassed, then an additional 
    £5 is charged as well as the amount the client went over the overdraft limit.'''
    def changing_title(self, new_title):
        self.title = new_title
    '''Method changes client title.'''
    def changing_first_name(self, new_first_name):
        self.first_name = new_first_name
    '''Method changes the first name.'''
    def changing_last_name(self, new_last_name):
        self.last_name = new_last_name
    '''Method changes the last name.'''

    def changing_preferred_pronoun(self, new_preferred_pronoun):
        self.preferred_pronouns = new_preferred_pronoun
    '''Method changes the pronouns.'''

    def changing_occupation(self, new_occupation):
        self.occupation = new_occupation

    '''Method changes the occupation.'''

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
    '''This method returns a client as a dictionary. So if a client was inputted as a dataframe into the class, it will
    be returned as a dictionary when this function is called using the client class object.'''