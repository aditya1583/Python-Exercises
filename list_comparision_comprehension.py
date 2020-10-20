#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
#LIST COMPARISION
#print([(a,b) for a in [1,2,3] for b in [3,4,5]])
# j = []
# for x in [1,2,3]:
#     for y in [3,4,5]:
#         if x != y:
#             j.append((x,y))
# print(j)
#PRINT DOUBLED VALUES
# vec = [-4, -2, 0, 2, 4]
# print([x*2 for x in vec])
#LIST TO EXCLUDE -VE #'s
#print([x*2 for x in vec if x >=0])
# USE THE abs(absolute) method
#print([abs(x) for x in vec])
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# print([wepon.strip() for wepon in freshfruit])
# create a list of 2-tuples like (number, square)
# print([(x,x**2) for x in range(10)])
# flatten a list using a listcomp with two 'for'
# l = []
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print([num for elem in vec for num in elem])
# # #Above is equal to below :)
# # for elem in vec:
# #     for num in elem:
# #         l.append(num)
# # print(l)
# from math import pi
# print([str(round(pi, i)) for i in range(1, 6)])
# NESTED LIST
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])
