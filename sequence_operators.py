subject = "he's "
adverb = "probably "
verb = "winning "
context = "in life "
attribute = "with that charisma "

print(subject + adverb + verb + context + attribute)

print("he's " "probably " "winning" " in life " "with that charisma")

print("Money " * 20)

today = "friday"

print("fri" in today)
print("day" in today)
print("nah" in today)
print("vacation" in today)

# another way to write code from line 13 to line 18 is 
'''
today = "friday"
# List of substrings to check
search_terms = ["fri", "day", "nah", "sun"]

for term in search_terms:
    print(f"Is '{term}' in '{today}'? {term in today}")
'''
