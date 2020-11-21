import os
import time


# print('operating system name:', os.name)
# print('current working directory:', os.getcwd())
# print('list files and directories in current working directory:',
#       os.listdir('.'))

# 测试文件是否存在：
# try:
#     file = open('a.txt', 'r')
#     text = file.read()
#     file.close()
# except IOError:
#     print('not accessed or problem in reading:', 'a.txt')

# ****************************************************************************
'''
Write a Python program to list only directories, files and all directories, 
files in a specified path.
'''


def list_only_dirs_or_only_files(path):
    print('file path:', path)
    get_all_files_and_dirs = os.listdir('../../python')
    print('all files and directories:', get_all_files_and_dirs)
    get_only_files = [name for name in get_all_files_and_dirs if os.path.isfile(os.path.join(path, name))]
    print('only files:', get_only_files)
    get_only_dirs = [name for name in get_all_files_and_dirs if os.path.isdir(os.path.join(path, name))]
    print('only directories:', get_only_dirs)


# list_only_dirs_or_only_files('../../python')

# ****************************************************************************
'''
Write a Python program to scan a specified directory and 
identify the sub directories and files.
'''


def identify_file_and_directory(path):
    print('path is:', path)
    for entry in os.scandir(path):
        if entry.is_dir():
            type = 'dir'
        elif entry.is_file():
            type = 'file'
        elif entry.is_symlink():
            type = 'link'
        else:
            type = 'unknown'
        print('{name} type is {type}'.format(name=entry.name, type=type))


# identify_file_and_directory("D:\python_projects\python")

# ****************************************************************************
'''
Write a Python program to check for access to a specified path. 
Test the existence, readability, writability and executability of the specified path
'''


def check_access_path(path):
    print('exist:', os.access("D:\python_projects\python", os.F_OK))
    print('readable:', os.access("D:\python_projects\python", os.R_OK))
    print('writable:', os.access("D:\python_projects\python", os.W_OK))
    print('executable:', os.access("D:\python_projects\python", os.X_OK))


# check_access_path('D:\python_projects\python')

# ***************************************************************************

stat_info = os.stat('D:\python_projects\python')
# print(stat_info.st_size)
# print(stat_info.st_mode)
# print(stat_info.st_uid)
# print(stat_info.st_dev)
# print(time.ctime(stat_info.st_ctime))
# print(time.ctime(stat_info.st_mtime))
# print(time.ctime(stat_info.st_atime))

# ****************************************************************************
'''
Write a Python program to create a symbolic link and 
read it to decide the original file pointed by the link
'''


def test_symlink():
    print(os.path.basename(__file__))
    # test_operating_system_service.py
    print(__file__) # 此文件的全路径名；
    path = 'D:\\' + os.path.basename(__file__)
    os.symlink(__file__, path)
    print(os.readlink(path))


# test_symlink()

# ****************************************************************************
'''
Write a Python program to retrieve the current working directory and 
change the dir (moving up one).
'''


def restrieve_directory():
    print('current directory:', os.getcwd())
    print('change the dir(moving up one):', os.pardir)
    os.chdir(os.pardir)
    print('current directory:', os.getcwd())
    print('change the dir(moving up one):', os.pardir)
    os.chdir(os.pardir)
    print('current directory:', os.getcwd())


# restrieve_directory()
# current directory: D:\python_projects\python\test_third_party_module
# change the dir(moving up one): ..
# current directory: D:\python_projects\python
# change the dir(moving up one): ..
# current directory: D:\python_projects

# ***************************************************************************
'''
Write a Python program to iterate over a root level path and 
print all its sub-directories and files, also loop over specified dirs and files.
'''


def loop_dirs_and_files():
    path = 'D:\\python_projects\python'
    # os.walk(path)---
    for root, dirs, files in os.walk(path):
        print(root)
        for dir in dirs:
            print(dir)
        for file in files:
            print(file)


# loop_dirs_and_files()

# ****************************************************************************
'''
Write a Python program to test whether a given path exists or not. 
If the path exist find the filename and directory portion of the said path.
'''


def test_file_exist():
    file = os.path.dirname(__file__) + '/abc.txt'
    print('file:', file)
    print('file exists or not:', os.path.exists(file))
    print('file basename:', os.path.basename(file))
    print('file dirname', os.path.dirname(os.path.join(file)))


# test_file_exist()
# file: D:\python_projects\python\test_third_party_module/abc.txt
# file exists or not: True
# file basename: abc.txt
# file dirname D:\python_projects\python\test_third_party_module

# ****************************************************************************
'''
Write a Python program to join one or more path components together 
and split a given path in directory and file.
'''


def split_file_and_join_file():
    path = os.path.dirname(__file__) + '/abc.txt'
    print('path is:', path)
    print('file and directory split:', os.path.split(path))
    print('file join directory:', os.path.join(os.path.dirname(__file__),
                                               'abc.txt'))


# split_file_and_join_file()
# path is: D:\python_projects\python\test_third_party_module/abc.txt
# file and directory split: ('D:\\python_projects\\python\\test_third_party_module', 'abc.txt')
# file join directory: D:\python_projects\python\test_third_party_module\abc.txt

# ****************************************************************************
'''
Write a Python program to write a string to a buffer and retrieve the value written,
 at the end discard buffer memory.
'''


def write_to_buffer():
    import io
    output = io.StringIO()
    output.write('dongxiang is a genius!')
    print('buffer get value:', output.getvalue())
    output.close()


# write_to_buffer()
# buffer get value: dongxiang is a genius!

# ***************************************************************************

