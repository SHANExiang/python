

# Write a Python program to hash a word.
soundx = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1,
          2, 6, 2, 3, 0, 1, 0, 2, 0, 2]


def hash_word():
    word = input('input the word be hashed:')
    word = word.upper()
    coded = word[0]
    for a in word[1:len(word)]:
        i = 65 - ord(a)
        coded = coded + str(soundx[i])
    print('the coded word is ', coded)


def test_ord_chr():
    print(ord('9'))
    print(chr(69))
    print(len(soundx))  # 26


if __name__ == '__main__':
    # hash_word()
    # input the word be hashed:dgsf34
    # the coded word is  D00105

    test_ord_chr()
