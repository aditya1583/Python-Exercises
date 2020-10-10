#!/bin/python3

def line():
    print("")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
line
print(a)
line
no=int(input("Enter a number between 0-100:"))
line
print(no)
line
if no <= 0:
        print("# should not be < 0")
        quit()
elif no >= 100:
        print("# should not be > 100")
        quit()
else:
    for i in a:
        if i not in b and i<no:
            b.append(i)

print("")
#l=list(set(b))
print(b)
