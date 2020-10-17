#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

"""
Task
Given an integer n, perform the following conditional actions:
 If 

is odd, print Weird
If
is even and in the inclusive range of to
, print Not Weird
If
is even and in the inclusive range of to
, print Weird
If
is even and greater than , print Not Weird
"""
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter a number: ").strip())
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

    