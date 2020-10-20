#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    query_score = student_marks[query_name]
    """
import numbers
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))