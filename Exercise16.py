#!/bin/python3
"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""



import random

x = []

## USE RANDOM.CHOICE TO PICK A CHARECTER FROM THE GIVEN LIST HERE 'A-Z' '0-9' AND SPECIAL CHARS

def get_exit():
    choice = str(input("\n\nWould you like to quit. x/X"))
    if choice == 'X' or choice == 'x':
        quit()

def hard():
    choice = int(input("\nEnter how many charetcters would you like to have created:"))
    for i in range(1, choice+1):
        x.append(random.choice('abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*'))

##  THIS WILL PRINT THE PASSWORD
    
    for i in x:
        print(i, end = "")
    get_exit()
    


def easy():
    choice = int(input("\nEnter the number of letters in password:"))
    for i in range(1,choice+1):
        x.append(random.choice('abcdefghijklmnopqrstuvwxyz'))

    for i in x:
        print(i, end='')
    get_exit()



## User input
        
while True:
    user = str(input("How would you like to have your password generated- Easy/Hard "))

    if user == "Easy" or user == "easy":
        easy()
    else:
        hard()

