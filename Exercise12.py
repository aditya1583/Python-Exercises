#!/bin/python3

"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
"""

# Import random function
import random

# Initialize 2 Arrays, 1 for generating a new list other for inserting first and last from the list a

a = []
b = []

# Define function
def first_last(num,range_num):

# Generate random numbers for list a    
    for i in range(1,num+1):
        a.append(random.randint(1,range_num))

    print("\nGenerated list is:\n",a)

# Determine length of list 'a'
    lenA = len(a)

# Append and insert into A
    b.append(a[0])
    b.insert(lenA-1,a[lenA-1])
    print("\nNew list with start and end is :\n",b)




# User input for number of list elements and range of numbers
num = int(input("Enter any number:"))
range_num = int(input("Enter a number to geerate a range, can be 25,67,45 anything"))
first_last(num,range_num)
