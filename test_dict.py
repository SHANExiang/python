import uuid

# 合并两个字典
# 第一种方式
x = {'name': 'dong', 'age': 10}
y = {'host': 'compute', 'id': uuid.uuid4()}

z = x.copy()
print('z==%s' % z, 'id(x)==%s' % id(x), 'id(z)==%s' % id(z))
# z=={'name': 'dong', 'age': 10} id(x)==2342080434368 id(z)==2342110319872
z.update(y)
print('z==%s' % z, 'id(z)==%s' % id(z))
# z=={'name': 'dong', 'age': 10, 'host': 'compute',
# 'id': UUID('e4379eb9-5d36-4018-baf6-b6d0b0572441')} id(z)==2689673090240
# update()是就地和并字典，z还是同样的内存地址

# 第二种方式，python3.5以上版本
z = {**x, **y}
print('z==%s' % z, 'id(z)==%s' % id(z))
# z=={'name': 'dong', 'age': 10, 'host': 'compute',
# 'id': UUID('2f06eb3b-b1f2-4b4b-9321-4a42f5b5f2d5')} id(z)==1376163448128
# z又存储到另一块内存

