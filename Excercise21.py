from itertools import islice
# def read_file(file):
#     x = open(file)
#     return(x.read())




# print(read_file('Just_test.txt'))
# print(read_file('Exercise1.py'))

#Just_test.txt
def read_n_lines(fname,line):
    with open(fname) as f:
        for i in islice(f,line):
            print(i)


read_n_lines('Just_test.txt',4)
