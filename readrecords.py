"Objectives"
"" '' # Import connect module
"" '' # Create a function to read record(s) from a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

from connect import *
def read_all_films():
    try:
       dbCon, dbCursor = db_access()

       # all_songs = dbCursor.execute("SELECT * FROM films").fetchall()
       # run the the dbCursor.execute() to select all records in the films table
       dbCursor.execute("SELECT * FROM tblFilms")

       #fetched all selected records using the fetchall method and assigned it to the all_films variable
       all_films = dbCursor.fetchall()

       if all_films:
           print("*" * 100)
           #fortmat output FilmID, Title, Release Year, Rating, Duration, Genre
           print(f"FilmID{'':<3}|Title{'':<25}|Release Year{'':<18}|Rating{'':<24}|Duration{'':<22}|Genre{'':10} ")
           print("*" * 100)

           for aFilm in all_films:
               "0     1        2       3"
               #1	Test	Tester	Testing
               print(f"{aFilm[0]:<9}|{aFilm[1]:<30}|{aFilm[2]:<30}||{aFilm[2]:<30}|{aFilm[2]:<30}|{aFilm[3]:<10}")
               print("-" * 100)
       else:
           print("No songs found in the films table")
    except  sql.OperationalError as oe:
        print(f"Failed to read because: {oe}")

if __name__ == "__main__":
    read_all_films()



