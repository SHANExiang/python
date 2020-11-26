from shutil import copyfile


def copy_file_to_another_file(  one_file, another_file):
    copyfile(one_file, another_file)


# copy_file_to_another_file('somefile.data', 'another.txt')
