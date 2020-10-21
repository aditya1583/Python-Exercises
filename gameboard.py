#!/usr/bin/python3
line = ' ---'
column = '|   '
n = int(input())
for i in range(n):
    print(n * line)
    print((n+1) * column)
print(line * n)