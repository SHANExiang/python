

def write_file(original_list, file_name):
    with open(file_name, 'w') as f:
        for x in original_list:
            f.write(str(x))


write_file([1, 2, 3, 4], 'somefile.data')
