#!/bin/python3

import random

"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

"""





## USE RANDOM.CHOICE TO PICK A CHARECTER FROM THE GIVEN LIST HERE 'A-Z' '0-9' AND SPECIAL CHARS

def get_exit():
    choice = str(input("\n\nWould you like to quit. x/X"))
    if choice == 'X' or choice == 'x':
        quit()

def hard():
    x = []
    choice = int(input("\nEnter how many charetcters would you like to have created:"))
    for i in range(1, choice+1):
        x.append(random.choice('1278abcdi!@#$%jklmnop3456qrefghstuvwxyz90^&*'))

##  THIS WILL PRINT THE PASSWORD
    
    for i in x:
        print(i, end = "")
    get_exit()
    


def easy():
    x = []
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

"""

def genStrongPassword():
    upperchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerchars = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    specialchars = "!@#$%^&*()"
    password = ''
    password = password + random.choice(upperchars)
    password = password + random.choice(lowerchars)
    password = password + random.choice(nums)
    password = password + random.choice(specialchars)
    password = password + random.choice(upperchars)
    password = password + random.choice(lowerchars)
    password = password + random.choice(nums)
    password = password + random.choice(specialchars)
    return(password)

def generateWeakPassword():
    defpass = [ '01234', '56789', 'abcdefg', 'hijklmn', 'opqrstuvezxy' ]
    return(random.choice(defpass))

print('Generating password 1', genStrongPassword())
print('Generating password 2', genStrongPassword())
print('Generating password 3', genStrongPassword())
print('Generating password 4', genStrongPassword())

answer = input('Do you want strong or weak password?')
if answer == 'strong':
    print('Your strong password is ',genStrongPassword())
elif answer == 'weak':
    print('Your weak password is ',generateWeakPassword())
else:
    print('ERROR, you have typed a wrong word, please try again typing "strong" or "weak"')
"""



    

    
