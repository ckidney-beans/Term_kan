import action
import board
import file_check


# Basic Menu
def menu():
    print("Terminal Kanban")
    print("1. View Board ")
    print("2. Create Task")
    print("3. Change Task Status")
    print("4. Create New Tile")
    print("5. Exit Menu")
    selection = input("Please make your section: ")

    choices = {1, 2, 3, 4, 5}

    print(selection)  # Here for testing
    action.action(selection)


file_check.file_check()
# Main if else statement for menu choice
menu()
