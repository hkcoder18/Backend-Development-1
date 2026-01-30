# Pandas
# Data Analysis, Data transformation, Data cleaning, Data manipulation, Handling csv files exels file
# pandas open source module
# Numpy + pandas mostly used module/librari AI/ML.

# import pandas as pd

# # Pandas core data structures
# # 1. Series
# # 2. Dataframe

# # 1. Series 
# # Series is similar to python list or numpy array
# # indexing means labels
# # One-dimensional

# lst = [12,3,45,67,89,77]
# s = pd.Series(lst)
# print("Series : ",s)

# lst = [12,89,77]
# s = pd.Series(lst, index=['a','b','c'])
# print("Series : ",s)

# # Accessing by index values

# lst = [12,89,77]
# s = pd.Series(lst, index=['a','b','c'])
# print("Index a :",s['a'])


# # Methods of series

# s = pd.Series([12,3,3,4,54,5,65,7,899])
# print("Sum : ",s.sum())
# print("Maximum : ",s.max())
# print("Minimum : ",s.min())

# Vector opration
# lst = [12,34,6,8]
# val = 5
# lst1=[]
# for i in lst:
#     lst1.append(i+val)
# print("After adding value : ",lst1)

# marks = [12,34,56,78]
# s = pd.Series(marks)
# print("Marks : ",s + 2)

# 2. Dataframe
# Dataframe rows + columns 

import pandas as pd
data = {
    "Name" : ["Ram","Om","Pratik","Divya"],
    "Age" : [22,21,23,24],
}
df = pd.DataFrame(data)
# print(df)

# Access Data through column name
data = {
    "Name" : ["Ram","Om","Pratik","Divya"],
    "Age" : [22,21,23,24],
    "marks" : [99,98,97,96]
}
df = pd.DataFrame(data)

# print(df["Name"])
# print(df[["Name","marks"]])

# Adding new column
df["roll_no"] = [1,2,3,4]

print("Data after adding column : ",df)

df["marks"] = df["marks"] + 1
print(df)
