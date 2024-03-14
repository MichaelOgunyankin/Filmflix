"Objectives"
"" '' # Import connect module
"" '' # Create a function to read record(s) from a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

from connect import *
def read_all_songs():
    try:
       dbCon, dbCursor = db_access()

       # all_songs = dbCursor.execute("SELECT * FROM songs").fetchall()
       # run the the dbCursor.execute() to select all records in the songs table
       dbCursor.execute("SELECT * FROM songs")

       #fetched all selected records using the fetchall method and assigned it to the all_songs variable
       all_songs = dbCursor.fetchall()

       if all_songs:
           print("*" * 100)
           #fortmat output SongID, Title, Artist, Genre
           print(f"SongID{'':<3}|Title{'':<25}|Artist{'':<24}|Genre{'':10} ")
           print("*" * 100)

           for aSong in all_songs:
               "0     1        2       3"
               #1	Test	Tester	Testing
               print(f"{aSong[0]:<9}|{aSong[1]:<30}|{aSong[2]:<30}|{aSong[3]:<10}")
               print("-" * 100)
       else:
           print("No songs found in the songs table")
    except  sql.OperationalError as oe:
        print(f"Failed to read because: {oe}")

if __name__ == "__main__":
    read_all_songs()



