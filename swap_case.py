"""
CONVERT CASE from an input string

"""
def swap_case(s):
    for i in s:
        if i == i.upper():
            l.append(i.lower())
        else:
            l.append(i.upper())
    return(str1.join(l))

l = []
if __name__ == '__main__':
    str1 = ""
    s = input("Enter a string to convert :\n")
    result = swap_case(s)
    print(result)