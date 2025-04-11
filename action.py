import board

tiles = ["To-Do", "In Progess", "Completed"]

def action(selection):
    print(selection)
    if selection == "1":
        board.view(tiles)
    # elif selection == 2
    #   task.create()
    # elif selection == 3
    #   task.status()
    # elif selection == 4
    #   board.create_tile()
    elif selection == "5":
        exit_program()
    else:
        print ("Improper selection.")
        print ("Please select again")
