import sqlite3 # import sqlite3 library

conn = sqlite3.connect("c5Music.db") # create and connect the db
cursor = conn.cursor() # cursor method iterate our db

import time

def updateSongs():
    # enter the id the needs to be update
    idField = int(input("Enter the Id of the record you want to update: "))
    # enter the name of the field needs to be change
    fieldName = input("Which field would you like to change(Title, Artist, Genre): ")
    newFieldValue = input("Enter the new value of the field: ")
    print(f"User Value {newFieldValue}")
    newFieldValue = "'" + newFieldValue + "'" 
    print(f"User amended input {newFieldValue}")

    try:
        cursor.execute(f"UPDATE songs SET {fieldName} = {newFieldValue} WHERE SongID = {idField} ")
        conn.commit()
        print(f"Record {idField} Updated")
        time.sleep(3)
        cursor.execute('SELECT * FROM songs')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print(f"Song {idField} not updated")
    finally:
        conn.close()
# update()
