#!/bin/python3
"""

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken, and when the game ends, print this out.





# Import Random library which will generate random integer
"""



import random

# Initialize a list 'a'
a = []
cnt = 0

# Loop until user quit's

while True:
    opt = str(input("Do you want to quit (y/n):"))
    if opt == "y" or opt=="Y":
        break

# Generate Random integer
    randnum = random.randint(1,9)

# Request user input
    num = int(input("\nGuess a number between 1 - 9:"))
    cnt+=1

# Append to list a and output when the user quits
    a.append(num)

# Validate if num is '>', '<' or '=' random number being gererated.

    if num == randnum:
        print("\nRight, random number generated in {}\n".format(randnum))
    elif num < randnum:
        print("\nNumber is Too low, since the num generated is {} \n".format(randnum))
    elif num > randnum and num < 10:
        print("\nNumber is Too high,num generated is {} \n".format(randnum))
    else:
        print("\nInvalid number selected\n")


# Print the list
print("You have taken {} guesses and Your numbers are".format(cnt),a)
