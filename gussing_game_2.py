#!/usr/bin/python3
import random

def check_num():
    n = int(input( """\n\n Guess a number between 0 - 100 FROM FUNCTION and enter \n\n """))
    return(n)


i = 0
n = (int(input( """\n\n Guess a number between 0 - 100 and enter \n\n """)))
l = []
rand = random.randint(0,100)
while True:
    # print("\n\n In while first, rand is {} and n is {} \n\n".format(rand,n))
    if n == rand:
        print("\n\n You got it the rand integer is, {} and you took {} attempts \n\n".format(rand,i))
        break
    elif n >= rand:
        print("Your guess is  high")
        i += 1
        n = check_num()
    elif n <= rand and n <= rand/2 and n <= rand/4:
        print("Your guess is too too low, go higher")
        i += 1
        n = check_num()
    elif n <= rand and n <= rand/2:
        print("your guess to too low, a bit higher please")
        i += 1
        n = check_num()
    elif n <= rand:
        print("Guess low")
        i += 1
        n = check_num()


    