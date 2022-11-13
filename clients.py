# Class for client_details
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

    def adding_in_account_balance(self, add_balance):
        new_balance = int(add_balance) + int(self.account_balance)
        self.account_balance = new_balance

    def removing_in_account_balance(self, removing_balance):
        if removing_balance > (self.account_balance + self.overdraft_limit):
            self.account_balance = (self.account_balance + self.overdraft_limit) - (removing_balance + 5)
        else:
            self.account_balance = (self.account_balance - removing_balance)

    def changing_title(self, new_title):
        self.title = new_title

    def changing_first_name(self, new_first_name):
        self.first_name = new_first_name

    def changing_last_name(self, new_last_name):
        self.last_name = new_last_name

    def changing_preferred_pronoun(self, new_preferred_pronoun):
        self.preferred_pronouns = new_preferred_pronoun

    def changing_occupation(self, new_occupation):
        self.occupation = new_occupation
