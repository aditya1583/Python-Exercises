#!/bin/python3

import datetime

def line():
    print("")

yr=datetime.datetime.now()
thisyr=yr.year

name = input("Enter name:")
age = int(input("Enter age:"))

old= (100-age)

yr100=(old+thisyr)
line()
print("Hi {}, you will turn 100 in the year {}".format(name,yr100))
line()

