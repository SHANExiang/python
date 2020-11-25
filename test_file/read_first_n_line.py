from itertools import islice


def read_n_line(file_name, nline):
    with open(file_name, 'r', encoding='utf-8') as f:
        print(islice(f, nline))
        for line in islice(f, nline):
            print(line)


read_n_line('somefile.data', 2)
