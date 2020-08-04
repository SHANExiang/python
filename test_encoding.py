# -*- coding:utf-8 -*-


x = '春香'
print(x)  # 春香
s = u'vdgfdghf 董'
print('type(s)==%s' % type(s), 'id(s)==%s' % id(s), s)
# type(s)==<class 'str'> id(s)==1782182021696 vdgfdghf 董
s1 = s.encode('gbk')
s2 = s.encode('utf-8')
s3 = s2.decode()
print('type(s1)==%s' % type(s1), 'id(s1)==%s' % id(s1), s1)
# type(s1)==<class 'bytes'> id(s1)==1782182900816 b'vdgfdghf \xb6\xad'
print('type(s2)==%s' % type(s2), 'id(s2)==%s' % id(s2), s2)
# type(s2)==<class 'bytes'> id(s2)==1782182903408 b'vdgfdghf \xe8\x91\xa3'
print('type(s3)==%s' % type(s3), 'id(s3)==%s' % id(s3), s3)
# type(s3)==<class 'str'> id(s3)==1993071642976 vdgfdghf 董

# 可以看到不同编码的字符串，存放在不同的内存地址，bytes类型字符串在python3中，是什么就打印什么
# s encode()之后再decode()已经不是之前的s了，重新放置再另一块内存
