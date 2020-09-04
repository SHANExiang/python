from __future__ import print_function
import sys


def stderr_test(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# stderr_test('abc', 'def', 'xyz', sep='-*-')   # abc-*-def-*-xyz


def stdin_test():
    print('please input your name:')
    name = sys.stdin.readline()
    print(name)


# 执行代码
#     stdin_test()

# output:
# please input your name:
# dongx
# dongx


def stdout_test():
    sys.stdout.write('hello' + '\n')


stdout_test() # 等价于print('hello' + '\n')
