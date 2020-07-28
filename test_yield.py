

def run():
    count = 0
    while True:
        n = yield count
        print(n, '----', count)
        count += 1


if __name__ == '__main__':
    gen = run()
    # print(next(gen))
    print(gen.__next__())
    gen.send('dx')
    gen.send('xiang')
