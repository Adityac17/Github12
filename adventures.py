available_exits = ["north", "south", "east", "west"]
# this is a escape game using while loop iteration
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please enter a direction to exit: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break

print("Phew you finally escaped the prison")
