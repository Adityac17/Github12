activity = input("What would you like you to do today? ")

if "playsole" not in activity.casefold():
    print("But i wanna go to playsole")
else:
    print("Yay! Let's go to playsole!")

'''
This is the 2nd way to type the code a bit more advanced 

# Define the target activity once
TARGET_ACTIVITY = "playsole"

activity = input("What would you like to do today? ")

if TARGET_ACTIVITY not in activity.casefold():
    print(f"But i wanna go to {TARGET_ACTIVITY}")
else:
    print(f"Yay! Let's go to {TARGET_ACTIVITY}!")

running this code will still give the same output as the one in lines 1 to 6
'''
