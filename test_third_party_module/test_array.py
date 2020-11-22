from array import *


# 定义一个integer类型的数组
arr = array('i', [1, 2, 3, 4, 5])
print(arr)  # array('i', [1, 2, 3, 4, 5])
arr.append(6)
print(arr) # array('i', [1, 2, 3, 4, 5, 6])
print(len(arr), arr.itemsize) # 6 4

# 迭代数组
for x in arr:
    print(x)

print('array to list:', arr.tolist())
# array to list: [1, 2, 3, 4, 5, 6]



