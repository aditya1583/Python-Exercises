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
