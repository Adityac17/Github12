# for i in range(1, 13):
#         print("No. of {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
#         print("*" * 80)

# print("-" * 80) 

name = input("Enter your name: ")
age = int(input("How old are you, {0} ? ".format(name)))
print(age)

if age>= 18:
    print("You are old enough to vote {0}".format(name))

else:
    print("Come back in {0} years {1}".format(18 - age, name))


if age<18:
    print("Come back in {0} years {1}".format(18 - age, name))

elif age == 900:
    print("You too old nigga die {0} you MF".format(name))
else:
    print("You are old enough to vote {0}".format(name))



