#!/usr/bin/python3

n = int(input())

def incr(num):
    return(num + 1)

def conv(mins):
    return(mins * 60)


def tri_area(base,height):
    return( (base * height)/2 )

print(incr(n)) # increments the num by 1
print(conv(n)) # convert min to seconds

def give_me_something(string):
    return("something {}".format(string))

h = int(input())
print(int(tri_area(n,h))) # Area of a triangle 
print(give_me_something("Bob Jane"))