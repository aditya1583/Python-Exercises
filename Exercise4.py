#!/bin/python3


print()
# User input
num=int(input("Enter a number to find all it's devisors:"))

# initiate 2 lists, 'l' is the first list to store all the numbers. 'final' is the list that the devisors go into

l=[]
final=[]

# input all numbers into the list 'l', exclude '0' and increment 'num'

for i in range(1,num+1):
    l.append(i)

# the above would create a list with all the number upto 'num' e.g. num=5 l=[1,2,3,4,5,6] 

# loop all the numbers in list 'l', if a number goes into num with a '0' reminder add it to 'final' list and print

for x in l:
    if num % x == 0:
        final.append(x)

print()
# Print the final output of divisors
print(final)
print()
        
        
    
