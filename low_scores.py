#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

if __name__ == '__main__':
    a= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([score, name])

    a.sort()
    b = [i for i in a if i[0] != a[0][0]]
    print(b)
    c = [j for j in b if j[0] == b[0][0]]
    print(c)
    c.sort(key=lambda x: x[1])
    for i in range(len(c)):
        print(c[i][1])



