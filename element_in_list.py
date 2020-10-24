#!/usr/bin/python3


def check(lst, el):
    for i in lst:
        if i == el:
            return(True)
        else:
            continue
    return(False)

print(check([2,3,4,6,7,8,9],100))
