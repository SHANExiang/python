import random

"""

"""


def read_random_line(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    return random.choice(lines)


print(read_random_line('somefile.data'))
