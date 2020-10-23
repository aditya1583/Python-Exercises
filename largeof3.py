"""
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements!
"""
#!/usr/bin/python3
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print("A is highest")
elif b > c and b > a:
    print("B is highest")
elif c > a and c > b:
    print("C is highest")
elif a == b == c:
    print("All equal")
