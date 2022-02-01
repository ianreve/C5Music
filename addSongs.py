import sqlite3 # import sqlite3 library

conn = sqlite3.connect("c5Music.db") # create and connect the db
cursor = conn.cursor() # cursor method iterate our db

import time

# create a subroutines to add songs
def addSongs():
    # create an empty list
    songs = []
    # song ID feild is auto increament 
  
    songID = cursor.lastrowid
    
    #capture the value from the user
    title = input("Enter song title: ")
    artist = input("Enter song artist: ")
    genre = input("Enter song genre: ")

    #append the capture values from the user 
    songs.append(songID)
    songs.append(title)
    songs.append(artist)
    songs.append(genre)

    try:
        # cursor.execute('INSERT INTO songs, SongID, Title, Artist, Genre VALUES(songID,title,artist,genre)',songs)
        cursor.execute('INSERT INTO songs VALUES(?,?,?,?)', songs)
        conn.commit()
        print("Song Added")
        time.sleep(3)
        cursor.execute('SELECT * FROM songs')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print(f"Song {title} not added")
    finally:
        conn.close()
        
# addSongs()