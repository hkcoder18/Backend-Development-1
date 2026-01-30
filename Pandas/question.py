# [12,3,6,8,9]
# [4,0,1,2,3]

nums = [10, 7, 2, 5, 9]
# result = [sum(1 for y in nums if y < x) for x in nums]
# print(result)
arr = []
for i in nums:#i = 7
    count = 0
    for j in nums:# j = 10
        if i==j:pass
        elif i>j:
            count = count + 1 #0
    arr.append(count) # [4]
print("List : ",arr)
