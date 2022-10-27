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

        #method explaining how data should be ordered
        def order(self):
            return (f"{self.title},{self.first_name},{self.last_name},{self.preferred_pronoun},{self.date_of_birth},{self.occupation},{self.account_balance},{self.overdraft_limit}")

#main
if __file__=="__main__":
    #creating an object of the class client_details
    client1= client_details('Ms', 'Skyler', 'Harrinson', 'they', '2/23/1960', 'Research and Development', '59', '5')

    #order details according to the method provided
    print(client1.order())