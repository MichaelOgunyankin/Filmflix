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
        search_field = input("Search by SongID or Title or Artist or Genre: ")

        if search_field == "SongID":
            #search by SongID
            song_id = int(input("Enter SongID: "))
            dbCursor.execute("SELECT * FROM songs WHERE SongID = ?", (song_id,))
            row = dbCursor.fetchone()

            if row is None:
                print(f"No record with SongID {song_id} exists in the songs table")

            else:
                print("*" * 100)
                print(f"SongID{'':<3}|Title{'':<25}|Artist{'':<24}|Genre{'':10}")
                print("*" * 100)
                print(f"{row[0]:<9}|{row[1]:<30}|{row[2]:<30}|{row[3]:<10}")
                print("-" * 100)
        
        elif search_field.title() in ["Title", "Artist", "Genre"]:
            #Search by Title or Artist or Genre
            str_input = input(f"Enter the value for the field {search_field}: ")
            
            dbCursor.execute(f"SELECT * FROM songs WHERE {search_field} LIKE ?", (f'%{str_input}%',))
            # ("SELECT * FROM songs WHERE ? LIKE ?", (search_field, f"%{str_input}%",))
            # or 
            # (f"SELECT * FROM songs WHERE {search_field} LIKE ?", (f'%{str_input}%',))
            # dbCursor.execute(f"SELECT * FROM songs WHERE {search_field} LIKE ?", (f"%{str_input}%",))
        

            rows = dbCursor.fetchall()

            if not rows:
                print(f"No record with field {search_field} matching {str_input} in the songs table")
            else:
                # display all matched records from the saongs table
                print("*" * 100)
                print(f"SongID{'':<3}|Title{'':<25}|Artist{'':<24}|Genre{'':10} ")
                print("*" * 100)
                for records in rows:
                    print(f"{records[0]:<9}|{records[1]:<30}|{records[2]:<30}|{records[3]:<10}")
                    print("-" * 100)
                  
        else:
            print(f"Search field {search_field} Invalid! ")
    except sql.OperationalError as e:
        print(f"Search error: {e}")
if __name__ == "__main__":
    report()

    