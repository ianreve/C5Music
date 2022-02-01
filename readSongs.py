import sqlite3 # import sqlite3 library

conn = sqlite3.connect("c5Music.db") # create and connect the db
cursor = conn.cursor() # cursor method iterate our db


def readSongs():
    cursor.execute("SELECT * FROM songs")
    row = cursor.fetchall()
    for record in row:
        print(record)
# readSongs()