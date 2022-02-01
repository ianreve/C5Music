import readSongs 
import addSongs 
import deleteSongs  
import updateSongs
import searchSongs


def menuOptions():
    options = 0
    list = ["1", "2", "3", "4", "5", "6"]
    while options not in list:
        print(
            '\nMenu Options:\n1. Print Songs\n2. Add Songs\n3. Update Songs\n4. Search Songs\n5. Delete Songs\n6. Exit '
        )

        options = input("Enter one options above : ")

        if options not in list:
            print("Not in the list")

    return options


mainProgram = True

while mainProgram == True:
    mainMenu = menuOptions()

    if mainMenu == "1":
        readSongs.readSongs()
    elif mainMenu == "2":
        addSongs.addSongs()

    elif mainMenu == "3":
        updateSongs.updateSongs()

    elif mainMenu == "4":
        searchSongs.searchSongs()

    elif mainMenu == "5":
        deleteSongs.deleteSongs()

    elif mainMenu == "6":
        mainProgram == False
input("Press enter to exit ")

# menuOptions()
