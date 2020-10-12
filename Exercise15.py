#!/bin/python3

"""Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
"""
b = []

def print_backwards(string):
## Split the string
        x = string.split()
        lenX = len(x)

## Print in reverse Order
        for i in range(lenX):
            lenX = lenX - 1
            b.append(x[lenX])
        print("in reverse:",b)

## User input        
string = str(input("Enter a sentence:"))
print_backwards(string)

