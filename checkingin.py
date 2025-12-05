parrot = "Norwegian Blue"

letter = input("Please enter a letter: ")
# string comparsion is case sensitive
if letter in parrot:
    print("{} is in {}".format(letter, parrot))

else:
    print("I don't need that letter ")
