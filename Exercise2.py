#!/bin/python3
"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

    ADDITIONAL FUNCTIONALITY TO LOOP CONTINEOUSLY 
"""

### Extra to loop until asked to exit

def def2num():
    if num % check == 0:
        print("{} devides evenly into {}".format(check,num))
    else:
        print("{} does not devide evenly into {},".format(check,num))


def evenodd():      

    #Validate even or odd
    
    #Validate if num is divisible by 4 and 2
    
    if num % 2 == 0 and num % 4 == 0:
        print("You entered {}, which is Even and is divisible by 4 and 2".format(num))
    #Validate if num is divisible only 2 to prove it's even
    elif num % 2 == 0:
        print("You entered {}, which is Even".format(num))
    #Print Odd since it is not divisible by 2
    else:
        print("You entered {}, which is odd".format(num))
        print('')
    

print('')

while True:
    print('')
    #Ask user input
    num=int(input("Enter a number:"))
    check=int(input("Enter another number:"))

    print('')
    #Ask user the choice
    tonum=int(input("Enter '1' for 2 numbers, '2' for validating even or odd, 3 to EXIT:"))

    #Validate choice
    
    if tonum == 1:
        def2num()
    elif tonum == 2:
        evenodd()
    else:
        if tonum == 3:
       # x=str(input(("Exit x/X? else hit 'Enter' ")))
       # if x == "x" or x == "X":
            break


    
    
