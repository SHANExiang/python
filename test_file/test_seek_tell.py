

def test_seek():
    import os
    file_size = os.stat('somefile.data').st_size
    print(file_size)  # 581  表示文件总字节数为581
    f = open('somefile.data', 'rb')
    print(f.tell())  # 当前文件指针位置为0字节
    f.readline()
    print(f.tell())  # 87 读取一行数据后文件指针位置为87字节
    f.seek(1)   # 表示从文件开头偏移一个字节
    print(f.tell())   # 此时文件指针位置字节数位1
    f.seek(20, 2)
    print(f.tell())   # 601 表示从文件末尾位置再正着往前走了20字节
    f.seek(-10, 1)
    print(f.tell()) # 591  表示从之前的601位置往后走了10字节，就是591了


test_seek()
