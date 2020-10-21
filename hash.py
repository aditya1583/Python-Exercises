
n = input()
input_line = input()
print(n)
input_line = input_line.split()
print(input_line)
for i in range(n):
        input_line[i] = int(input_line[i])
t = tuple(input_line)
print(t)
print(hash(t))