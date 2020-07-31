import re

s = 'sagddgdfdgfdgxxxxxx'
print(re.match('s(.*)x', s).group(0))

str1 = "Python's features"
str2 = re.match( r'(.*)on(.*?).*', str1, re.M|re.I)
print(str2.group(1))
