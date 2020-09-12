import os
import struct
import sys


# Write a Python program to determine whether a Python
# shell is executing in
# 32bit or 64bit mode on OS?
def get_os_mode_32bit_or_64bit():
    return struct.calcsize("P") * 8


# Write a Python program to get OS name, platform and
# release information
def get_os_name():
    import platform
    return os.name, platform.system(), platform.release()


# Write a Python program to locate Python site-packages.
def get_python_site_packages():
    import site
    return site.getsitepackages()


# Write a python program to call an external command in Python.
def command_to_call():
    import subprocess
    return subprocess.call(['python', '--version'])


# Write a python program to get the path and name of the file that is
# currently executing
def get_file_path_the_current_execute():
    print(__file__)
    return os.path.realpath(__file__)


# Write a Python program to find out the number of CPUs using
def get_cup_numbers_using():
    import multiprocessing
    return multiprocessing.cpu_count()


# Write a Python program to list all files in a directory in Python
def get_all_files_list_from_direction():
    files_list = [f for f in os.listdir('F:\projects\python')
                  if os.path.isfile(os.path.join('F:\projects\python', f))]
    directions_list = [f for f in os.listdir('F:\projects\python')
                       if not os.path.isfile(os.path.join
                                             ('F:\projects\python', f))]
    return files_list, directions_list


# Write a python program to access environment variables.
def get_environment_variables():
    print(os.environ)
    print(os.environ['PATH'])
    print(os.environ['OS'])


def get_absolute_file_path(path_fname):
    return os.path.abspath(path_fname)


def get_create_time_or_modify_time_of_file():
    import time
    print('last modified:%s' % time.ctime(os.path.getmtime('os_module_test_42.py')))
    print('create time:%s' % time.ctime(os.path.getctime('os_module_test_42.py')))


def get_copyright_info():
    import sys
    print(sys.copyright)


def test_whether_the_system_is_a_big_endian_platform_or_little_endian_platform():
    import sys
    print(sys.byteorder)
    if sys.byteorder == 'little':
        print('Little-endian platform.')
    else:
        print("Big-endian platform.")


# test_whether_the_system_is_a_big_endian_platform_or_little_endian_platform()
# output:
# little
# Little-endian platform.


def test_get_object_size_in_bytes():
    st1 = 'one'
    st2 = 'two'
    st3 = 'three'
    print('st1 is %s, ' % st1, "it\'s size %s bytes" % sys.getsizeof(st1))
    print('st1 is %s, ' % st2, "it\'s size %s bytes" % sys.getsizeof(st2))
    print('st1 is %s, ' % st3, "it\'s size %s bytes" % sys.getsizeof(st3))


# test_get_object_size_in_bytes()
# output:
# st1 is one,  it's size 52 bytes
# st1 is two,  it's size 52 bytes
# st1 is three,  it's size 54 bytes


def test_getrecursionlimit():
    print('递归深度限制为==%s' % sys.getrecursionlimit())


# test_getrecursionlimit()
# output:
# 递归深度限制为==1000


def test_clear_screen_or_terminal():
    import os
    import time
    os.system('cls')
    time.sleep(2)


# test_clear_screen_or_terminal()


def test_os_path():
    import os.path

    for file in [__file__, os.path.dirname(__file__), '/', './broken_link']:
        print('File        :', file)
        print('Absolute    :', os.path.isabs(file))
        print('Is File?    :', os.path.isfile(file))
        print('Is Dir?     :', os.path.isdir(file))
        print('Is Link?    :', os.path.islink(file))
        print('Exists?     :', os.path.exists(file))
        print('Link Exists?:', os.path.lexists(file))


# test_os_path()
# output:
# File        : F:/projects/python/w3resource/os_module_test_42.py
# Absolute    : True
# Is File?    : True
# Is Dir?     : False
# Is Link?    : False
# Exists?     : True
# Link Exists?: True
# File        : F:/projects/python/w3resource
# Absolute    : True
# Is File?    : False
# Is Dir?     : True
# Is Link?    : False
# Exists?     : True
# Link Exists?: True
# File        : /
# Absolute    : True
# Is File?    : False
# Is Dir?     : True
# Is Link?    : False
# Exists?     : True
# Link Exists?: True
# File        : ./broken_link
# Absolute    : False
# Is File?    : False
# Is Dir?     : False
# Is Link?    : False
# Exists?     : False
# Link Exists?: False

print(os.listdir(os.path.dirname(__file__)))
import glob
print(glob.glob("*"))


if __name__ == '__main__':
    # print(get_os_mode_32bit_or_64bit())   # 64

    # print(get_os_name())  # ('nt', 'Windows', '10')

    # print(get_python_site_packages())

    # command_to_call()  #  Python 3.8.1

    # print(get_file_path_the_current_execute()) # F:\projects\python\w3resource\os_module_test_42.py

    # print(get_cup_numbers_using())  # 6

    # print(get_all_files_list_from_direction())

    # get_environment_variables()

    # import getpass
    # print(getpass.getuser())  # Administrator

    # import socket
    # print(socket.gethostname())  # PC201910292213
    # print(socket.gethostbyname_ex(socket.gethostname()))  # 获得当前主机的所有ip列表
    # ('PC201910292213', [], ['172.30.64.1', '192.168.176.17', '192.168.73.1', '192.168.49.1', '192.168.31.58'])
    # print(socket.gethostbyname(socket.gethostname()))  # 192.168.31.58
    # print(socket.gethostbyname_ex(socket.gethostname())[2])
    # ['172.30.64.1', '192.168.176.17', '192.168.73.1', '192.168.49.1', '192.168.31.58']
    # lis = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]
    # print(lis) # ['172.30.64.1']
    # print([socket.socket(socket.AF_INET,socket.SOCK_DGRAM)])
    # for s in [socket.socket(socket.AF_INET,socket.SOCK_DGRAM)]:
    #     print(s)
        # < socket.socket fd = 768, family = AddressFamily.AF_INET, type = SocketKind.SOCK_DGRAM, proto = 0 >
        # print((s.connect(('8.8.8.8', 53)),s.getsockname()[0], s.close()))
        # (None, '192.168.31.58', None)

    # print([l for l in (lis, [[(s.connect(('8.8.8.8', 53)),s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
    # 172.30.64.1

    # print(get_absolute_file_path('os_module_test_42.py'))
    # F:\projects\python\w3resource\os_module_test_42.py

    # get_create_time_or_modify_time_of_file()
    # last modified:Tue Sep  8 22:54:09 2020
    # create time:Thu Sep  3 21:53:40 2020
    # get_copyright_info()
    # Copyright (c) 2001-2019 Python Software Foundation.
    # All Rights Reserved.
    # Copyright (c) 2000 BeOpen.com.
    # All Rights Reserved.
    # Copyright (c) 1995-2001 Corporation for National Research Initiatives.
    # All Rights Reserved.
    # Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
    # All Rights Reserved.
    pass
