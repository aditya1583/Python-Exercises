#!/bin/python3
import random


"""

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

# initialize lists

a = []
b = []
z = []

# Generate 14 random numbers and add to lists a and b // alternativly ask user for 2 numbers

num1=int(input("Enter a random number a:"))
num2=int(input("Enter a random bumber b:"))

for i in range(1,num1+1):
    n=random.randint(2,50)
    a.append(n)

for i in range(1,num2+1):
    x=random.randint(2,50)
    b.append(x)

# Print lists a and b

print()
print("First list:",a)
print()
print("Second list:",b)
print()

# Check to see the intersection of lists
for x in a:
    if x in b:
        z.append(x)

# Convert list to dict to eliminate duplicates
mylist = list(dict.fromkeys(z))
print(mylist) 


        

