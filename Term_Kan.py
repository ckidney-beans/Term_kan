#importing files for functions used in the program
import board
import task

#setting default values as we do not know how to load or save a file yet.
#This will be changed out at later date
tiles = ["To-Do", "In Progess", "Completed"]
tasks = []

# Basic Menu
def menu():
    print ("Terminal Kanban")
    print ("1. View Board ")
    print ("2. Create Task")
    print ("3. Change Task Status")
    print ("4. Create New Tile")
    print ("5. Exit Menu")
    selection = input("Please make your section: ")

    choices = {1,2,3,4,5}

    print (selection)  #Here for testing
    action (selection)

menu()

# Main if else statement for menu choice
def action(selection):
    if selection in choices:
        for selection == 1
            board.view(tiles)
        elif selection == 2
            task.create()
        elif selection == 3
            task.status()
        elif selection == 4
            board.create_tile()
        elif selection == 5
            exit_program()
        else:
            print ("Improper selection.")
            print ("Please select again")
            menu()

# Program exit function.
exit_program()
    print ("Thank you")
    exit()
