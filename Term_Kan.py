#importing files for functions used in the program
import board
import action
# import task

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
    action(selection)

# Main if else statement for menu choice
menu()
# Program exit function.
def exit_program():
    print ("Thank you")
    quit()
