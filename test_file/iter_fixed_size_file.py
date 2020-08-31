from functools import partial

# 如果文本文件，一行一行读取更普遍些
# with open('somefile.data', 'rt') as f:
#     f.read()


# 如果是二进制文件，读取到固定大小的记录中更普遍
# RECODE_SIZE = 16
# with open('somefile.data', 'rb') as f:
#     records = iter(partial(f.read, RECODE_SIZE), b'')
#     for x in records:
#         print(x)
# records 对象是一个可迭代对象，它会不断的产生固定大小的数据
# 块，直到文件末尾。
# 在例子中，functools.partial 用来创建一个每次被调用时从文件中读取固定数
# 目字节的可调用对象。标记值 b'' 就是当到达文件结尾时的返回值。


# iter() 函数有一个鲜为人知的特性就是，如果你给它传递一个可调用对象和一个
# 标记值，它会创建一个迭代器。这个迭代器会一直调用传入的可调用对象直到它返回标
# 记值为止，这时候迭代终止。

f = open('somefile.data', 'rt', encoding='utf-8')
record = iter(partial(f.read, 3), '')
for x in record:
    print(x)