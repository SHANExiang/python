import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        print("{}: {}".format(label, (end_time - start_time)))


with timethis('counting'):
    n = 100000
    while n > 0:
        n -= 1

# output:
# counting: 0.022169828414916992


@contextmanager
def list_transaction(origin_list):
    working = list(origin_list)
    yield working
    origin_list[:] = working


if __name__ == '__main__':
    origin_list = [1, 2, 3, 4, 5]
    with list_transaction(origin_list) as lis:
        lis.append(6)
        lis.append(7)
    print(origin_list)

    try:
        with list_transaction(origin_list) as lis:
            lis.append(8)
            lis.append(9)
            raise RuntimeError('oops')
    except:
        pass
    print(origin_list)
