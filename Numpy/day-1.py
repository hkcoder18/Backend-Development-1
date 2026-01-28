# Pyhton For Data science
# Numpy and Pandas

# Numpy
# 1. Numpy stands for numeric python
# 2. Purpose : Array based computing, mathamematical operations
# https://numpy.org/
#
# Difference list vs numpy
# Fast processsing (numpy>>list) 
# Memory numpy takes less memory than list

# lst = [1,2,3,4,5,6]
# print("Type of list : ",type(lst))
# print("List : ",lst)

# # import statement
# import numpy as np

# arr = np.array(lst)
# print("Type of array : ",type(arr))
# print("Array : ",arr)

# # -----------------------------------------------------
# lst = [1,2,4,5,89]
# print("Type of list : ",type(lst))
# print("List : ",lst)
# for i in lst:
#     print(type(i))

# arr = np.array(lst)
# print("Type of array : ",type(arr))
# print("Array : ",arr)
# for i in arr:
#     print(type(i))

# ------------------------------------------------------

import sys
lst = [12,23,34,56,67,89,809,78,9009,7,77,7,6,76,76,76,776,76,7,76,67,12,23,34,56,67,89,809,78,9009,7,77,7,6,76,76,76,776,76,7,76,67]
print("Size of list : ",sys.getsizeof(lst))

import numpy as np
arr = np.array(lst)
print("Size of array : ",sys.getsizeof(arr))

# ---------------------------------------
lst = [10,23,345,5678,779,98]

# for i in lst:
#     print(f"Value : {i} Address : {id(i)}")

# ndarray - reshape
lst = [10,23,345,5678,779,98]

arr = np.array(lst)
print("Array : ",arr)

print(arr.reshape(2,3))
print(arr.reshape(3,2))