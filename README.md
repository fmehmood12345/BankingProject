# 1034 Project 2 - Farheen Mehmood
Just bullet-pointing for now so that I know what to put in each section:
### <u>Overview of the project</u>
I have 3 different python files in this project clients, banking_application and CSV.

The clients class only has functions which will edit attribute which the client will have control over in a real life scenario. For example, the client shouldn't be able to change their date of birth or their overdraft limit. They also should only be able to add to or withdraw money from their account not change the account balance.

In my banking application class, I have 8 functions:
1. `__fetch_csv_dataframe()` : This is to fetch and return the dataframe which contains all the data from the CSV file so that we can manipulate it.
2. `print_current_CSV_file()`: This is a function to print out the csv dataframe once it has been fetched using the *__fetch_csv_dataframe()* function.
3. `__return_client_df_as_dict()`: This function will change the dictionary called into the parameter into a dataframe.
4. `retrieving_a_client()`: In this function, I retrieve a client by comparing the firstname, lastname and date of birth with other clients in the CSV dataframe.
5. `accounts_with_negative_balance()`: This function retrieves all clients which have a negative account balance from the csv dataframe.
6. `deleting_a_client()` : The functions compares the first_name, last_name and date_of_birth which will be called into the function with the Firstname, Lastname and Date of Birth from the dataframe and deletes that client from the dataframe. It then runs the refresh_csv_file function in the CSV class which will update the csv file.
7. `changing_overdraft_limits()`: Just like *deleting_a_client()*, first_name last_name and date_of_birth is called into the function, however in this function, a new overdraft limit is also called in. The called in firstname, lastname and date birth is compared with the Firstname, Lastname and Date of Birth from the database and then the overdraft limit is changed to the new overdraft limit which is called in.
8. `adding_a_client()`: This will take a client dictionary as an argument and turn it into a dataframe. Then a concat method is used to join the csv dataframe and the dataframe of the new client together. Then a function called *refresh_csv_file* is called to write the updated dataframe to the csv file. 
9. `searching_by_firstname()`: This is a function which first check if the inputted firstname is equal to any of the firstnames in the CSV file. If there is a client with the inputted firstname then code is run to output all information on that client. Otherwise, a print statement is run which states that a client with the passed firstname does not exist in the CSV file.
10. `searching_by_lastname()`: This function searches the dataframe of the CSV file for clients with the same firstname as the one called into the function, if they match then code to return all the details of the client is run otherwise an else statement is run which will print an error saying that the client with the lastname inputted into the function doesn't exist.
11. `searching_by_date_of_birth()`: This function searches the dataframe of the CSV file for clients with the date of birth equal to the inputted date of birth in the function. If there is no date of birth equal to the inputted date of birth then a print statement is run which will state that a client with date of birth called into the function doesn't exist. Otherwise, details of all the clients with that date of birth are outputted. 

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
### <u>Specific use case examples of how to run this application</u> 
<u> How to run functions in the banking application class</u>

1. *`print(BA_Obj.retrieving_a_client("Wilma","Huniwall","4/04/2000"))`*  this is an example of how retrieve a client. You have to use the object of the banking application class and call the retrieving_a_client function. When calling the function, pass through the firstname, lastname and date of birth. This is because the firstname, lastname and date of birth are compared with all clients in the CSV dataframe so that the correct client is retrieved. Finally, use the print statement to print out the client.
2. *`print(BA_Obj.searching_for_accounts_with_negative_balance())`* this is an example of how to retrieve negative balance. An object of the banking application is used to call this function as well however, for this function, nothing is required to pass through into the parameters. The print statement is used to print out the return of this function.
3. *`BA_Obj.deleting_a_client("Alice","Liddyard","8/09/1978")`* this is an example of how to delete a client from the CSV file. Call the function using the banking application object and pass through the firstname, lastname and date of birth of the client that is required to be deleted. Then to check if the client is deleted, you can use the *BA_Obj.print_current_CSV_file()* function to print out the CSV file in the form of a dataframe.
4. *`BA_Obj.changing_overdraft_limits("Skyler","Harrinson","2/07/1960","1560")`* this is an example of how to change the overdraft limits. First, call the function using the banking application object and pass in the firstname, lastname, date of birth and the amount you want the new overdraft limit to be. You can check if the overdraft limit has changed running the code *BA_Obj.print_current_CSV_file()*.
5. *`BA_Obj.adding_a_client(client_object.return_client_dict())`* First, a client object is made and all required data is filled out. This is called into the *return_client_dict()*. The return of this function is called into the *adding_a_client()* function. However, to be able to call this function, an object of the banking application class has to be made first.
6. *`print(BA_Obj.searching_by_firstname("Wilma"))`* To search by firstname, first make an object of the banking application class and use that to call the *searching_by_firstname()* function. Then pass the firstname of the client or clients that are required to be called in the parameter. Then use the print statement to print out all details of that specific client.
7. *`print(BA_Obj.searching_by_lastname("Huniwall"))`* To search by lastname, use an object of the banking application class to be able to call the function *searching_by_lastname()* and pass in the lastname of the client or clients that are needed to be called. Use the print statement to display all the details of the client.
8. *`print(BA_Obj.searching_by_date_of_birth("10/04/1979"))`* Search the date of birth through passing in the date of birth of the clients or client you want details on. Use the banking application object to call this function. The print statement will output all the details

<u> How to run the functions in the client class </u>

First have a dictionary of all the details of the client you want to add. Then made an object for the client class so that you can call the functions in that class. I used this dictionary to test the client class functions I have made. However, when *BA_Obj.retrieving_a_client("Wilma","Huniwall","4/04/2000")* is run, you can call the functions in the client class by making a client class object and passing the received client into the parameter. 

`client = {
        "title": 'Mr',
        "first_name": 'Gerald',
        "last_name": 'Smith',
        "preferred_pronouns": 'he/him',
        "date_of_birth": '15/12/1990',
        "occupation": 'Software Engineer',
        "account_balance": 100,
        "overdraft_limit": 10
    }`

`client_object = client_class(**client)`

1. `client_object.changing_title("Mrs")`  : This function is to change the title of the client. Simple call the function using the client class object and then pass in the new title in the parameter
2. `client_object.changing_first_name("Susan")` : This function is the change the first name of the client. Call the function using an object and pass in the new first name of the client.
3. `client_object.changing_last_name("Blunt")`: This function is the change the last name of the client. Call the function using an object and pass in the new last name of the client.
4. `client_object.changing_preferred_pronoun("she/her")`: This function is the change the preferred pronouns of the client. Call the function using an object and pass in the new preferred pronouns of the client.
5. `client_object.changing_occupation("Designer")`:This function is the change the occupation of the client. Call the function using an object and pass in the new occupation of the client.
6. `client_object.removing_in_account_balance(100)`: This function withdraws money from the account balance. If the amount removed is more than the account balance plus the overdraft limit then the account balance will go into negatives and an extra £5 is charged. The class object is used to call the function and the amount withdrawed is passed as a parameter.
7. `client_object.adding_in_account_balance(200)`: The class object will call the function and the deposit amount is passed into the parameter. Then the account balance and incremented by the deposit amount.
