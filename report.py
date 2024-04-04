"Objectives"
"" '' # Import connect module
from connect import *
"" '' # Create a function to run sql statements to generate different type of reports


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

# Create a function to run sql statements to generate different type of reports
def report():
    try:
        dbCon, dbCursor = db_access()

        # ask for the search field 
        search_field = input("Search by FilmID or Title or Year Released or Rating or Duration or Genre: ")

        if search_field == "filmID":
            #search by FilmID
            film_id = int(input("Enter FilmID: "))
            dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (film_id, ))
            row = dbCursor.fetchone()

            if row is None:
                print(f"No record with FilmID {film_id} exists in the films table")

            else:
                print(row)  # print the single record found as per song_id            
            # else:
            #         print("*" * 100)
            #         print(f"FilmID{'':<3}|Title{'':<25}|Release Year{'':<18}|Rating{'':<24}|Duration{'':<22}|Genre{'':10}")
            #         print("*" * 100)
            #         print(f"{row[0]:<9}|{row[1]:<30}|{row[2]:<30}|{row[3]:<10}|{row[4]:<3}|{row[5]:<10}")
            #         print("-" * 100)
        elif search_field in ["YearReleased","Duration"]:
            int_input = int(input(f"Enter the {search_field}: "))
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {search_field} = ?", (int_input, ))
            results = dbCursor.fetchall()
            for aresult in results:
                print(aresult)  

        elif search_field.title() in ["Title", "Rating", "Genre"]:
            str_input = input(f"Enter the {search_field}: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {search_field} = ?", (str_input, ))
            results = dbCursor.fetchall()
            for aresult in results:
                print(aresult)              

    # Search by Title or Year Released or Rating or Duration or Genreif search_field.title() == "Year Released":

        # Handle year released specifically (assuming year is an integer)try:

            #tr_input = input(f"Enter the year released: ")  # Prompt for integer year            search_query = f"SELECT * FROM tblFilms WHERE yearReleased = ?"  # Use exact match            dbCursor.execute(search_query, (str_input,))        except ValueError:

            # print("Invalid year entered. Please enter a valid integer year.")

        else:
            print(f"Invalid {search_field} entered. Please enter a valid field.")
        # Search other fields using LIKE operator for partial matches
        # elif search_field.title() in ["Title", "Year Released", "Rating", "Duration", "Genre"]:
        #     #Search by Title or Release Year or Rating or Duration or Genre
        #     str_input = input(f"Enter the value for the field {search_field}: ")
            
        #     dbCursor.execute(f"SELECT * FROM tblFilms WHERE {search_field} LIKE ?", (f'%{str_input}%',)) 
        #     # search_query = f"SELECT * FROM tblFilms WHERE {search_field} = ?"
        #     # dbCursor.execute(search_query, (str_input,))



        #     # ("SELECT * FROM songs WHERE ? LIKE ?", (search_field, f"%{str_input}%",))
        #     # or 
        #     # (f"SELECT * FROM songs WHERE {search_field} LIKE ?", (f'%{str_input}%',))
        #     # dbCursor.execute(f"SELECT * FROM songs WHERE {search_field} LIKE ?", (f"%{str_input}%",))
        

        #     rows = dbCursor.fetchall()

        #     if not rows:
        #         print(f"No record with field {search_field} matching {str_input} in the films table")
        #     else:
        #     # display all matched records from the saongs table
        #         for records in rows:
        #             print(records)
        # else:
        #     print(f"Search field {search_field} Invalid! ")
    except sql.OperationalError as e:
        print(f"Search error: {e}")


if __name__ == "__main__":
    report()
#             else:
#                 # display all matched records from the films table
#                 print("*" * 100)
#                 print(f"FilmID{'':<3}|Title{'':<25}|Release Year{'':<18}|Rating{'':<24}|Duration{'':<22}|Genre{'':10}")
#                 print("*" * 100)
#                 for records in rows:
#                     # print(f"{records[0]:<9}|{records[1]:<30}|{records[2]:<30}|{records[3]:<10}|{row[4]:<3}|{row[5]:<10}")
#                     print(f"{records[0]:<9}|{records[1]:<30}|{records[2]:<30}|{records[3]:<10.1f}|{records[4]:<3}|{records[5]:<10}")
#                     print("-" * 100)
                  
#         else:
#             print(f"Search field {search_field} Invalid! ")
#     except sql.OperationalError as e:
#         print(f"Search error: {e}")
# if __name__ == "__main__":
#     report()

    