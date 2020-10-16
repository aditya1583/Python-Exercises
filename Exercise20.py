#!/bin/python3

"""
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

    Use binary search.
"""

import random

def exit_func():
    choice = str(input("Enter X for exit:"))
    if choice == 'x' or choice == 'X':
        quit()

def numpresent():
    for i in a:
        if i == uinput2:
            b.append(i)
    if len(b) == 0:
        print("\nFalse, {} is not present in the list ".format(uinput2))
    else:
        print("\nTrue,  {} is present in the list ".format(uinput2))
        
    


def gen_rand(uinput1):
     for i in range(1,uinput1+1):
         a.append(random.randint(1,99))
     sortA = list(dict.fromkeys(sorted(a)))
     print(sortA)
     numpresent()
     exit_func()   
     

while True:
    #i = 0
    a = []
    b = []
    uinput1 = int(input("Enter the numbers you want to generate:"))
    uinput2 = int(input("Enter the number that you would like to search from the list:"))
    print(gen_rand(uinput1))
