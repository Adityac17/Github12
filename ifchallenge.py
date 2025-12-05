name = input("Please enter you name: ")
age = int(input("Ppleas eenter your age: "))

if 18 < age < 30:
    print("Welcome {} to Club Mahindra holiday home".format(name))
elif age <= 18:
    print(f"C'mon nigga you to young for this {name} ")
else:
    print(f"You to old for this shit {name}")