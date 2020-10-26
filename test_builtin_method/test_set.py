l = [1, 2, 3, 4, 10]
t =(2, 4, 8, 11, 15)

s1 = set(l)
s2 = set(t)
# print('s1==%s' % s1, 's2==%s' % s2, sep='\n', end='dong\n')
# 相同的元素
# print(s1 - s2) # s1中有s2中没有的元素
# print(s1 + s2)# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(s2 - s1) # s2中有s1中没有的元素
# print(s1 & s2) # {2, 4}   s1与s2的交集
# print(s1 ^ s2) # {1, 3, 8, 10, 11, 15}  两者总和去掉交集元素
# print(s1.union(s2))


def absent_digits(n):
  all_nums = set([0,1,2,3,4,5,6,7,8,9])
  n = set([int(i) for i in n])
  print(n)
  n = n.symmetric_difference(all_nums)
  n = sorted(n)
  return n


print(absent_digits([9,8,3,2,2,0,9,7,6,3]))
