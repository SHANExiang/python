# list类的sort方法进行排序，且还是原列表的顺序
lis1 = [1, 2, 3, 4, 2, 7, 3]
lis2 = list(set(lis1))
lis2.sort(key=lis1.index)
# print(lis2)
# [1, 2, 3, 4, 7]
# 使用sorted函数
# print(sorted(lis2, key=lis1.index))

# 遍历进行排序
lis3 = list()
for x in lis1:
    if x not in lis3:
        lis3.append(x)
# print(lis3)


# Write a Python program to remove the first item from a specified list.
def remove_first_item_from_specified_list():
    color = ["Red", "Black", "Green", "White", "Orange"]
    print("\nOriginal Color: ",color)
    del color[0]
    print("After removing the first color: ", color)
    color.pop(0)
    print("After pop the first color: ", color)


# remove_first_item_from_specified_list()
# Original Color:  ['Red', 'Black', 'Green', 'White', 'Orange']
# After removing the first color:  ['Black', 'Green', 'White', 'Orange']
# After pop the first color:  ['Green', 'White', 'Orange']


# ****************************************************************************
import builtins
print(builtins.__dict__, len(builtins.__dict__), sep='\n')
