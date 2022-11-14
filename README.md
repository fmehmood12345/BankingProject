# c1012346_csc1034_project2_2022-

### Overview of the project
I have 3 different python files in this project. One is specifically to manage the CSV file which has a CSV class in it. I have one function, *dataframe_of_csv_file()*, in the CSV class which reads from the csv file and adds the content of the
csv file into a dataframe. I also have another function, *refresh_csv_file()* , which will override the data in the csv file with the updated dataframe so that changes are shown in the 
csv file. 
In my banking application class, I have 8 functions:
1. __fetch_csv_dataframe() : This is to fetch the dataframe which contains all the data from the CSV file so that we can manipulate it.
2. print_current_CSV_file(): This is a function to print out the csv dataframe so that I can check if data is changed as I wanted.
3. __return_client_df_as_dict(): This is a function I have made to change a client dataframe to a dictionary so that it can go into my clients file and be presented in the form I wanted it in.
4. retrieving_a_client(): In this function, I retrieve a client from the dataframe I've made of the CSV file and then pass it through the __return_client_df_as_dict() function which will present it as required.
5. accounts_with_negative_balance(): This function retrieves all clients which have a negative account balance from the csv dataframe.
6. deleting_a_client() : The functions compares the first_name, last_name and date_of_birth which will be called into the function with the Firstname, Lastname and Date of Birth from the dataframe and deletes that client from the dataframe. It then runs the refresh_csv_file function in the CSV class which will update the csv file.
7. changing_overdraft_limits(): Just like *deleting_a_client()*, first_name last_name and date_of_birth is called into the function, however in this function, a new overdraft limit is also called in. The called in firstname, lastname and date birth is compared with the Firstname, Lastname and Date of Birth from the database and then the overdraft limit is changed to the new overdraft limit which is called in.
8. adding_a_client():
### Assumptions made when building the application

### How to run the application

### a specific example "use case" describing how you would use the application with input data -> Ask Auzan