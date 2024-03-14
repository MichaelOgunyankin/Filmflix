"Objectives"
"" '' # Import connect module
from connect import *
"" '' # Create a function to update record(s) in a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement
# Create a function to update record(s) in a table in a database
def update_record():
    try:
        dbCon, dbCursor = db_access()

        # check if the FilmID exists
        film_id = int(input("Enter FilmID to update a record: "))
        dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?",(film_id,))

        row = dbCursor.fetchone()

        if row == None:# if there is no match with the film_id provided
            print(f"No recod with FilmID {film_id} exists in the table films")

        else:# if there is a match with the film_id provided
            num_fields = input("Enter N to update one field or Y to update all fields: ").upper()

            if num_fields == "Y":
                # update all fields  
                film_title = input("Enter film title: ")
                year_released = int(input("Enter release year: "))
                film_rating = input("Enter rating: ")
                film_duration = int(input("Enter duration: "))
                film_genre = input("Enter genre: ") 

                # perform update 
                dbCursor.execute("UPDATE tblFilms SET title =?, yearReleased=?, rating=?, duration=?, genre=? WHERE SongID =?",(film_title,year_released,film_rating, film_duration, film_genre,film_id))
                dbCon.commit()
                print(f"All fields in the record {film_id} updated in the films table")

            elif num_fields == "N":
                #ask for the field to be updated 
                field_name = input("Enter the field (Title or Release Year or  Rating or Duration or Genre): ").title()
                if field_name not in ["Title", "Release Year", "Rating", "Duration", "Genre"]:
                    print(f"Field {field_name} not a valid field name in the table")
                else:
                    #ask for the field value
                    field_value = input(f"Enter the value for the field {field_name}: ")
                    # perform update  on a specific field
                    dbCursor.execute(f"UPDATE tblFilms SET {field_name} =? WHERE filmID =?", (field_value, film_id,))
                    dbCon.commit()
                    print(f"Record {film_id} updated in the films table")
            else:
                print("Invalid choice, please enter Y or N")
    except sql.OperationalError as e:
        print(f"Update failed: {e}")
if __name__ == "__main__":
    update_record()
