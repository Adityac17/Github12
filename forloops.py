parrot = "Norwegian Blue"

for character in parrot:
    print(character)
    
# Renamed 'number' to 'raw_input_string' for clarity
raw_input_string = input("Please enter a series of number with anyu no of separators you like: ")
sep = ""

for char in number:
    if not char.isnumeric():
        sep = sep + char
# another way to write line 12 is separator_list.append(char) which does exactly the same thing
print(sep)
