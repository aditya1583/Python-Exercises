#!/bin/python3
#
"Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it."

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



# Method 1 [List Comprehension]:
b = [x for x in a if x % 2 == 0]

print(b)



# Method 2

b =[]

for x in a:
    if x % 2 == 0:
        b.append(x)

print(b)
