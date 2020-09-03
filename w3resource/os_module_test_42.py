import os
import struct


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


if __name__ == '__main__':
    # print(get_os_mode_32bit_or_64bit())   # 64
    # print(get_os_name())  # ('nt', 'Windows', '10')
    # print(get_python_site_packages())
    # command_to_call()  #  Python 3.8.1
    # print(get_file_path_the_current_execute()) # F:\projects\python\w3resource\os_module_test_42.py
    # print(get_cup_numbers_using())  # 6
    print(get_all_files_list_from_direction())




