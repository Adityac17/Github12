# parrot = "Norwegian Blue"

# for character in parrot:
#     print(character)

number = input("Please enter a series of number with anyu no of separators you like: ")
sep = ""

for char in number:
    if not char.isnumeric():
        sep = sep + char

print(sep)
