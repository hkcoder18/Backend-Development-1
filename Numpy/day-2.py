# Arithemetic Operations in Numpy
# addtion, subtraction, multiplication, division
# mod power

# Addition
lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = lst1 + lst2 # [1,2,3,4,5,6]
print("List Addition : ",lst3)

import numpy as np
arr1 = np.array(lst1)
arr2 = np.array(lst2)
arr3 = np.add(arr1,arr2)
print("Numpy Array Addition : ",arr3)

# Subtraction
arr1 = [10,15,23,89]
arr2 = [3,5,7,9]

arr3 = np.subtract(arr1,arr2)
print("Substration : ",arr3)

# Multiplication
arr1 = [1,2,3,4,5]
arr2 = [2,5,3,7,8]

arr3 = np.multiply(arr1,arr2)
print("Multiplication : ",arr3)

# Multiple array operation
arr1 = [1,2,3,4]
arr2 = [2,3,4,5]
arr3 = [4,2,6,8]
arr4 = [3,7,1,9]
result = np.add(np.add(arr1,arr2),np.add(arr3,arr4))
print("Result : ",result)

# Division
arr1 = [10,20,30,40]
arr2 = [2,5,3,8]
arr3 = np.divide(arr1,arr2)
print("Divide : ",arr3)

# mod
arr1 = [10,20,30,40]
arr2 = [2,5,3,8]
arr3 = np.mod(arr1,arr2)
print("Mod : ",arr3)

# power
arr1 = [10,20,30,40]
arr2 = [2,3,2,1]
print("Power of values : ",np.power(arr1,arr2))

# Statistical Operations

data = [23,45,67,89,12,34,56,78,90,11,22,33,44,55,66,77,88,99]
print("Max : ",max(data))
arr1 = np.array(data)
print("Maximum : ",np.amax(arr1))


data = [23,45,67,89,12,34,56,78,90,11,22,33,44,55,66,77,88,99]
print("Min : ",min(data))
arr1 = np.array(data)
print("Minimum : ",np.amin(arr1))


marks = [75,56,89,99,37]
# how to find mean(average) value
# total sum of values/ total number of values
percentage = sum(marks)/len(marks)
print("Percentage : ",percentage)

arr1 = np.array(marks)
print("Mean : ",np.mean(arr1))

# median
scores = [23,45,67,89,12,34,56]
# [12,23,34,45,56,67,89]
aar1 = np.array(scores)
print("Median : ",np.median(aar1))

scores = [12,4,5,18,56,7,88,79,34,100]
arr1 = np.array(scores)
print("Median : ",np.median(arr1))

from scipy import stats
# mode
arr1 = np.array([1,2,2,3,4,4,4,5,5,6,7,8,8,9])
print(stats.mode(arr1))

print(stats.mode([12,23,34,33,5,45,]))