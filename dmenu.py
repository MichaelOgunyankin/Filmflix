"Objectives"
"" '' # Import all CRUD modules
import addrecord, readrecords, updaterecord, deleterecord, report
"" '' # Create a function to read from a text file
"" '' # Display contents from a text file
"" '' # Use the Sequence, Selection and Iteration programming construct

 # Create a function to read from a text file
def read_file(file_path):# file_path is the parameter
    try: 
        with open(file_path) as open_file:
            #read the file content and save it in a variable called rf
            rf = open_file.read()# read()reads the content of the file

            return rf
    except FileNotFoundError as not_found:
        print(f"File not found {not_found}")

# # test read_file function 
# print(read_file("PtDBOps2024V2/dbMenu.txt"))
        
def films_menu():
    option = 0 # create an integer variable call option
    # create a list data structure hold string items/values and assign it to optionsList
    optionsList = ["1","2","3","4","5","6"]

    # call/invoke invoke the read_file funcion and assign it to a variable 
    menu_choices = read_file("Week 10/Day 4/Python Project/Filmflix/dbMenu.txt")

    # display the contents held in the menu_choices repeatedly 
    while option not in optionsList:
        print(menu_choices)

        # re-assign the options variable to accept string user input 
        option = input("Enter an option from the menu choices above: ") # "1"/"2"/"4.5..6.."

        # check if the value entred and stored in the option variable is in the optionsList
        if option not in optionsList:
            print(f"{option} is not a valid choice! ")
    return option

# create boolean variable 
main_program = True # can be toggle to False if required(to exit the loop below)

while main_program: #same as while True
    # call/invoke invoke the songs_menu() funcion and assign it to a variable

    menu_options = films_menu() # songs_menu() returns = "1"/"2"/"4.5..6.."

    # check if "1"/"2"/"4.5..6.." =="1"
    if menu_options == "1":
        # call the file name readrecords and the function read_all_songs() 
        readrecords.read_all_films()

        # check if "1"/"2"/"4.5..6.." =="2"
    elif menu_options == "2":
        # call the filename addrecord and the function insert_record()
        addrecord.insert_record()
    elif menu_options == "3":
        updaterecord.update_record()
    elif menu_options == "4":
        deleterecord.delete_film()
    elif menu_options == "5":
        report.report()
    else: #re-assign the value to False to exit the loop
        main_program = False
input("Press enter to exit: ")




