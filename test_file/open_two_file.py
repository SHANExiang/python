

def corresponding_two_file(file_name1, file_name2):
    """
    Write a Python program to combine each line from first file with the corresponding line in second file.
    :param file_name1:
    :param file_name2:
    :return:
    """

    with open(file_name1, 'r', encoding='utf-8') as f, \
            open(file_name2, 'r', encoding='utf-8') as g:
        for line1, line2 in zip(f, g):
            print(line1 + line2)


corresponding_two_file('somefile.data', 'words.txt')
