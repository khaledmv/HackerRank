# import math
# import os 
# import random
# import re
# import sys



## find min max sum within 1, 3, 5, 7, 9 = 16, 24


# def minMax(arg):
# 	x = sum(arg)
# 	return x

# num = [1,2,3,4,5,1,4,5]
# result = minMax(num)
# print(result)


def miniMaxSum(arr):
    # Write your code here
    x = sum(arr)
    return ((x-(max(arr))), (x-(min(arr))))

num = [1, 3, 5, 7, 9]

result = miniMaxSum(num)
print(result)


def minMax(arr):
	x = sum(arr)
	return ((x-max(arr))), (x-(min(arr)))

result = miniMaxSum(num)
print(result)



x = max("Mike", "John", "Vicky")

print(x)
 
y = min("Mike", "John", "Vicky")

print(y)

x = max(1,3,5,7,9)

print(x)


list_num = [1,3,5,7,9]

y = sum(list_num)

max_num = (y-max(list_num))

min_num = (y-min(list_num))

print(max_num)
print(min_num)