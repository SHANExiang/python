l = [1, 2, 3, 4, 10]
t =(2, 4, 8, 11, 15)

s1 = set(l)
s2 = set(t)
print('s1==%s' % s1, 's2==%s' % s2, sep='\n', end='dong\n')
# 相同的元素
print(s1 - s2) # s1中有s2中没有的元素
# print(s1 + s2)# TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(s2 - s1) # s2中有s1中没有的元素
print(s1 & s2) # {2, 4}   s1与s2的交集
print(s1 ^ s2) # {1, 3, 8, 10, 11, 15}  两者总和去掉交集元素

