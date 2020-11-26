


"""
Write a python program to find the longest words.
"""


def find_longest_word(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read().split()
    max_len = len(max(data, key=len))
    return [word for word in data if len(word) == max_len]


print(find_longest_word('words.txt'))

