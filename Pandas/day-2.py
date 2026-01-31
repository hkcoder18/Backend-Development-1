# CSV File Handling through pandas dataframe
# csv - comma sperated values
# csv file has extension .csv

import pandas

data = pandas.read_csv("Backend-Development-1\Pandas\data.csv")
print(data)
print("-------------------------------------------------------")
# function on csv

# 1. head()
# to see first 5 rows
rows = data.head()
print(rows)

print("-------------------------------------------------")

# data = pandas.read_csv("Backend-Development-1\Pandas\data.csv",usecols=["name","city"])
# print(data.head())

# 2. info()
# info is used to give the informtion about the data
print(data.info())

# write data to csv
data = {
    "Name" : ["Gayatri","Vishal","Kunal"],
    "Age" : [21,22,23]
}

df = pandas.DataFrame(data)
df.to_csv("Backend-Development-1/Pandas/info.csv")
print("Data successfully writen")

# update csv
student = {
    "Name" : ["Harshal"],
    "Age" : [23]
}
df = pandas.DataFrame(student)
df.to_csv("Backend-Development-1/Pandas/info.csv", mode='a',header=False)
print("Data successfully updated")


data = {
    "Name":["Harshal","Gayatri","Ram","Shital"],
    "Age" : [21,22,23,24],
    "City" : ["Pune","Nagpur","Akola","Pune"]
}

df = pandas.DataFrame(data)
df.to_csv("information.csv",index=False)
print("File write successfully")

student = {
    "Name" : ["Rahul"],
    "Age" : [22],
    "City" : ["Pune"]
}
df = pandas.DataFrame(student)
df.to_csv("information.csv",mode='a',header=False,index=False)
print("File Update Successfully")

# 2 rocerds
# 1 Add 1 delete 1 update read