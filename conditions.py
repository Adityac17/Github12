age = int(input("how old are you? "))

# if age >= 16 and age <= 65:               # and - if both conitions true then true otherwise false
#    print("Have a great day at work :) ") # or - if any 1 condition true then true, both true then true, both false then false

# if 16 <= age <= 65:
if age in range(16, 66): #note that line 6 is the most efficient way to write this is just another eay of writing the code
    print("Have a great day at work")
else:
    print("Enjoy your free time")

print('-'*67)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

