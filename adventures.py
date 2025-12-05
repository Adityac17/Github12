available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Pleas eenter a direction to exit: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break

print("Phew you finally escaped the prison")