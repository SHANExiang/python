import os


"""
Write a Python program to read last n lines of a file.
"""


def read_last_n_line(file_name, nline):
    buffer_size = 8192
    file_size = os.stat(file_name).st_size
    iterable = 0
    with open(file_name, encoding='utf-8') as f:
        if buffer_size > file_size:
            buffer_size = file_size - 1
            data = list()
            while True:
                iterable += 1
                f.seek(file_size - buffer_size*iterable)
                data.extend(f.readlines())
                if len(data) >= nline or f.tell() == 0:
                    print(''.join(data[-nline:]))
                    break


read_last_n_line('somefile.data', 4)
