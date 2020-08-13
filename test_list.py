# list类的sort方法进行排序，且还是原列表的顺序
lis1 = [1, 2, 3, 4, 2, 7, 3]
lis2 = list(set(lis1))
lis2.sort(key=lis1.index)
print(lis2)
# [1, 2, 3, 4, 7]
# 使用sorted函数
print(sorted(lis2, key=lis1.index))

# 遍历进行排序
lis3 = list()
for x in lis1:
    if x not in lis3:
        lis3.append(x)
print(lis3)

