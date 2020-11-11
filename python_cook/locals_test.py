

def test():
    a = 10
    loc = locals()
    print(type(loc))
    exec('b = a + 1')
    b = loc['b']
    print(b)


def test1():
    a = 10
    loc = {'a': a}
    glb = {}
    exec('b = a + 1', glb, loc)
    # print(glb)
    print(loc)


if __name__ == '__main__':
    # test()

    test1()
