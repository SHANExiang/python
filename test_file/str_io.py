import io
import sys


# print(sys.getdefaultencoding()) # utf-8


def test_io():
    str_obj = io.StringIO()
    str_obj.write('Hello World\n')
    print(str_obj.getvalue()) # Get all of the data written so far
    # # 将This is a test_id追加到文件对象str_object中
    print('This is a test_io', file=str_obj)
    print(str_obj.getvalue()) # Get all of the data written so far

    str_obj1 = io.StringIO('dongxiang is s gaenius!')
    print(str_obj1.read(4))
    print(str_obj1.read())
    byte_obj = io.BytesIO()
    byte_obj.write(b'binary data')
    print(byte_obj.getvalue())

# 执行代码
# test_io()


# output:
# Hello World
#
# Hello World
# This is a test_io
#
# dong
# xiang is s gaenius!
# b'binary data'



if __name__ == '__main__':
    test_io()
