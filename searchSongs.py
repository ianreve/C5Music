import sqlite3 # import sqlite3 library

conn = sqlite3.connect("c5Music.db") # create and connect the db
cursor = conn.cursor() # cursor method iterate our db




def searchSongs():
    # #enter id of recond to be updated
    # idField = input("Enter the ID of the record you want to update ")
    #enter the name of the field to perform the search on
    fieldName = input("Which field would you like to Search (Title, Artist, Genre)? ")
    # enter the value of the field to be updated 
    searchValue =  input("Enter the Search value for the field: ")
    print("User Value", searchValue)
    searchValue = "'" + searchValue + "'"
    print("User amended input", searchValue)

    try:
        cursor.execute("SELECT * FROM songs WHERE " + fieldName + "=" + searchValue)
        conn.commit()

        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
         print("Song " + searchValue + " Not found")
    finally:
        conn.close()
# searchSongs()






