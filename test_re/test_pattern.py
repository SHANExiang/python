import re


"""
Write a Python program to check that 
a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
"""


def compile_a_z_A_Z_0_9(string):
    pattern = re.compile(r'[^a-zA-Z0-9.]')
    string = pattern.search(string)
    return not bool(string)


print(compile_a_z_A_Z_0_9('ABCDEFabcdef123450')) # True
print(compile_a_z_A_Z_0_9('(*&&')) # False

