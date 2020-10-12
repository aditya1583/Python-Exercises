#!/bin/python3
"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

import random

a = []

# Function to remove duplicates

def rem_dups():
    b = set(a)
    print("New list without Dupes:",b)

# Function to generate random #'s

def gen_rand(x):
    for i in range(1,x+1):
        a.append(random.randint(1,x))
    print("Original List is :",a)

# user input
x = int(input("Enter a num:"))

gen_rand(x)
rem_dups()


