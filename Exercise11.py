#!/bin/python3

"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
"""

factors=[]


def isprime():
    num = int(input("Enter a number:"))
    if num != 0:
        for i in range(1, num + 1):
            if num % 2 == 0:
                factors.append(num / i)
        if len(factors) > 2:
            print("This is not prime #s")
        else:
            print("This is a prime #:")
            isprime()
    #return(factors)

isprime()
print(factors)
