# 1034 Project 2 - Farheen Mehmood
Just bullet-pointing for now so that I know what to put in each section:
### <u>Overview of the project</u>
I have 3 different python files in this project: clients, banking_application and CSV.

The clients class only has functions which will edit attribute which the client will have control over in a real life scenario. For example, the client shouldn't be able to change their date of birth or their overdraft limit. They also should only be able to add to or withdraw money from their account not change the account balance.

In my banking application class, I have 8 functions:
1. __fetch_csv_dataframe() : This is to fetch the dataframe which contains all the data from the CSV file so that we can manipulate it.
2. print_current_CSV_file(): This is a function to print out the csv dataframe so that I can check if data is changed as I wanted.
3. __return_client_df_as_dict(): This is a function I have made to change a client dataframe to a dictionary so that it can go into my clients file and be presented in the form I wanted it in.
4. retrieving_a_client(): In this function, I retrieve a client from the dataframe I've made of the CSV file and then pass it through the __return_client_df_as_dict() function which will present it as required.
5. accounts_with_negative_balance(): This function retrieves all clients which have a negative account balance from the csv dataframe.
6. deleting_a_client() : The functions compares the first_name, last_name and date_of_birth which will be called into the function with the Firstname, Lastname and Date of Birth from the dataframe and deletes that client from the dataframe. It then runs the refresh_csv_file function in the CSV class which will update the csv file.
7. changing_overdraft_limits(): Just like *deleting_a_client()*, first_name last_name and date_of_birth is called into the function, however in this function, a new overdraft limit is also called in. The called in firstname, lastname and date birth is compared with the Firstname, Lastname and Date of Birth from the database and then the overdraft limit is changed to the new overdraft limit which is called in.
8. adding_a_client(): This will take a client dictionary as an argument and turn it into a dataframe. Then a concat method is used to join the csv dataframe and the dataframe of the new client together. Then a function called *refresh_csv_file* is called to write the updated dataframe to the csv file. 
NOT SURE HOW MUCH DETAIL TO PUT IN SO THIS IS INCASE NOT MUCH DETAIL IS REQUIRED: *This function joins the client dataframe and the csv dataframe together and then writes this to the csv file to update it by calling the *refresh_csv_file* function.*

Finally, I have a CSV class which has 2 functions. The first function creates a dataframe of the entire CSV file. This is so that I can manipulate the data in the file without directly interfering with the CSV file. Then to update the CSV file after changes have been made, I have another function which will add my dataframe to the CSV file. I have called this function everytime a client has to be edited so that it will update in the CSV file as well. 
### <u>Assumptions made when building the application</u>
1. client class is responsible for editing only certain attributes e.g. clients only have control over editing firstname, lastname, pronouns, occupation, adding and withdrawing money from account. 
2. the bank can add clients, delete clients, retrieve clients, change overdraft limits, search by firstname and lastname, search by date of birth, search by negative account balance and print out all clients. Ideally, the clients class only has functions which only a client will have control over in real life.
3. cvs class is responsible to simply retrieving the csv file as a dataframe and then update the csv file once the data has been manipulated.
### <u>How to run the application</u>
1. python version 3.11
2. pandas
3. pip
4. complete setup of virtual environment
### <u>a specific example "use case" describing how you would use the application with input data</u> -> Ask