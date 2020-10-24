#!/usr/bin/python3
"""
Maximum of number without max function
"""
def difference_max_min(lst):
    # x = max(lst)
    # y = min(lst)
    # return(x - y)
    maxm = lst[0]
    for num in lst:
        if maxm < num:
            maxm = num
    return(maxm)


lst = [ 0, 4, 1, 4, -10, -50, 32, 21]
print(difference_max_min(lst))


# # def get_first_value(number_list):
# # 	return(number_list[0])
	
# # number_list = [5,1,2,34]
# # print(get_first_value(number_list))

# # def animals(chickens, cows, pigs):
# #     	return((chickens * 2) + (cows * 4) + (pigs * 4))

# # print(animals(1,2,3))
	
# def to_int(txt):
#     return(int(txt))

# def to_str(num):
# 	return(str(num))

# print(to_int("77") )
# print(to_str(77))
