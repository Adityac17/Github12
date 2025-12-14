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

# After learning more about Python i have figured out another way to write this program
"""
def print_parrot_chars(text):
    for character in text:
        print(character)

def extract_separators(input_string):
    separator_list = []
    for char in input_string:
        if not char.isnumeric():
            separator_list.append(char)
    return "".join(separator_list)

# Main Execution Guard
if __name__ == "__main__":
    parrot = "Norwegian Blue"
    print_parrot_chars(parrot)

    raw_input_string = input("Please enter a series of number with any no of separators you like: ")
    result = extract_separators(raw_input_string)
    print(result)
    """
