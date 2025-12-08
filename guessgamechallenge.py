import random
# this guessing game is the base version of the more complicated where the machine has to guess a number between 1 to 1000 under 10 guesses
highest = 10
answer = random.randint(1, 10)
print(answer) # TODO: Remove after testing
g = 0
print("please guess a number between 1 & 10: ")

while g != answer:
    g = int(input())

    if g == answer:
        print("You've guessed it finally")
        break
    else:
        if g < answer:
            print("Please guess higher")
        else:   #this condition shows the g > answer
            print("Please guess lower")

        # g = int(input())
        # if g != answer:
        #     print("Better Luck next time ")
        # else:
        #     print("You've guessed it finally")


