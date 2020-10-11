#!/bin/python3

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

name1 = str(input("Enter your name:"))
name2 = str(input("Enter your name:"))


while True:
    userA=str(input("\nHi {} Enter Either Rock-Paper-Scissors:".format(name1)))
    userB=str(input("\nHi {} Enter Either Rock-Paper-Scissors:".format(name2)))

    if userA == userB:
        print("Draw\n")
    elif userA == "Rock" and userB == "Scissors":
        print("{} Wins\n".format(name1))
    elif userA == "Paper" and userB == "Scissors":
        print("{}, wins \n".format(name2))
    elif userA == "Scissors" and userB == "Rock":
        print("{}, Wins\n".format(name2))
    elif userA == "Scissors" and userB == "Paper":
        print("{}, Wins\n".format(name1))
    elif userA == "Paper" and userB == "Rock":
        print("{}, Wins\n".format(name1))
    elif userA == "Rock" and userB == "Paper":
        print("{}, wins\n".format(name2))
    else:
        print("Invalid Entry\n")

    opt=str(input("Would you like to quit? 'Yes/No' :"))
    if opt == 'Yes' or opt == 'YES':
        print("Thanks for playing\n")
        break
    else:
        print("Happy playing\n")
