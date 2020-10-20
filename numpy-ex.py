#!/usr/local/bin/python3
"""
    Program to test all functions of list- APpend, remove, insert,pop,remove, sort and reverse

"""
l = []
def verify(x,y):
    opt = input("\nYou entered Position is {}, Number to insert is {}\n. Are you sure Yes/No:".format(x,y))
    if opt == "Yes" or opt == "YES" or opt == "yes":
        x = int(x)
        y = int(y)
        l.insert(x,y)
        print(l)
    else:
        x, y = input("\nInput Enter a position and number to insert:\n").split()
        verify(x,y)
        
while True:
    if __name__ == '__main__':
        N = int(input("""Enter your choice

        1.Insert
        2.Print
        3.Remove
        4.Append
        5.Sort
        6.Pop
        7.Reverse
        8.Exit \n\n:::""" ))
        if N == 1:
            x, y = input("\nInput Enter a position and number to insert:\n").split()
            verify(x,y)
        elif N == 2:
            print(l)
        elif N == 3:
            print(l)
            x = int(input("Enter the number from the list to remove:"))
            l.remove(x)
            print(l)
        elif N == 4:
            print(l)
            x = int(input("Enter a number to append to the list:"))
            l.append(x)
            print(l)
        elif N == 5:
           l.sort()
           print(l)
        elif N == 6:
            l.pop()
            print(l)
        elif N == 7:
            print(l)
            l.reverse()
            print(l)
        else:
            break

