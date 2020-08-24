import bz2
import gzip


# 以文本形式读取压缩文件
with gzip.open('somefile.gz', 'rt') as f:
    f.read()

with bz2.open('somefile.bz2', 'rt') as f:
    f.read()

# 以文本形式写入压缩数据
with gzip.open('somefile.gz', 'wt') as f:
    f.write()

with bz2.open('somefile.bz2', 'wt') as f:
    f.write()


# gzip.open() 和 bz2.open() 接受跟内置的
# open() 函数一样的参数，包括 encoding，errors，newline 等等。

# 它们可以作
# 用在一个已存在并以二进制模式打开的文件上。比如，下面代码是可行的：
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()



