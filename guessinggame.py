import random

highest = 10
answer = random.randint(1, 10)
print(answer) # TODO: Remove after testing

# print("please guess a number between 1 & {}: ".format(highest))
# g = int(input())


count= ""
while count != answer:
    print("please guess a number between 1 & {}: ".format(highest))
    g = int(input())
    if g < answer:
        print("Please guess lower")
        continue

    elif g > answer:
        print("Please guess higher")
        continue
    
    else:
        print("You've finally guessed it")
    


# if g != answer:
#     if g < answer:
#         print("Please guess higher")
#     else:   #this condition shows the g > answer
#         print("Please guess lower")

#     g = int(input())
#     if g == answer:
#         print("You've finally guessed it")
#     else:
#         print("Better Luck next time ")
# else:
#     print("You've guessed it the first time")









# if g != answer:
#     if g < answer:
#         print("Please guess higher")
#     else:   #this condition shows the g > answer
#         print("Please guess lower")

#     g = int(input())
#     if g == answer:
#         print("You've finally guessed it")
#     else:
#         print("Better Luck next time ")
# else:
#     print("You've guessed it the first time")





