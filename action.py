import board
import task

tiles = ["To-Do", "In Progess", "Completed"]


# Program exit function.
def exit_program():
    print("Thank you")
    quit()


def action(selection):
    print(selection)
    if selection == "1":
        board.view(tiles)
    elif selection == "2":
        task.create()
    # elif selection == "3":
    # task.status()
    # elif selection == "4":
    # board.create_tile()
    elif selection == "5":
        exit_program()
    else:
        print("Improper selection.")
        print("Please try again!")
        quit()
