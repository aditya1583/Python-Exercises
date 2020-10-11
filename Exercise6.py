#!/bin/python3

"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""


#  a = ['A', 'd', 'i', 't', 'y', 'a' ] 
#  b = ['a', 'y' ,'t', 't', 'd', 'A' ]

# Initialize 2 Arrays

a=[]
b=[]

# User input string

string=str(input("Enter a String:"))


# Convert to lower [ can be uppercase as well ]
stringl=string.lower()


# Read string and append to list a

for i in stringl:
    a.append(i)

# Find length of a
lengthA=len(a)


# Insert it into list b in reverse order
for x in a[-lengthA:]:
    b.insert(0,x)

print()

# Evaluate lists a and b

if a==b:
    print("{}, is a palindrome".format(string))
else:
    print("{}, is not a palindrome".format(string))



print()
