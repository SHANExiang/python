import time


def func():
    print("one------------->")
    yield 1
    print("two------------->")
    yield 2
    print("three----------->")
    yield 3
    print("four------------>")
    yield 4

# 执行代码
# 生成器就是个迭代器，有__iter__和__next__属性
# print(hasattr(func(), '__next__')) # True
# print(hasattr(func(), '__iter__')) # True


# 生成器模拟Linux下tail -f a.txt | grep 'error' | grep '404'

def tail(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        f.seek(0, 2) # 停到末尾开头 1从当前位置  2从文件末尾
        while True:
            line = f.readline()
            if line: # 如果有内容就读出
                yield line # 遍历时停在此行,并且将其返回值传递出去
            else:
                time.sleep(0.5) # 如果文件为空,休眠等待输入


def grep(generator, pattern): # generator为生成器类型
    for line in generator:  # 遍历生成器
        if pattern in generator:
            yield line

############################################################################

# 执行代码
# gen1 = grep(tail('test.txt'), 'error') # 动态跟踪文件新添加的内容,并且过滤出有patterns的行
# gen2 = grep(gen1, '404')  # gen1为生成器

# for x in gen2:   # 通过for循环来隐式调用__next__()方法
#     print(x)


def foo():
    while True:
         x = yield
         print('x==%s' % x)


# f = foo()
# print(next(f)) # None 程序运动到yield就卡住，等待下一个next
# f.send('dong') # x==dong给yield发送值dong,然后这个值被赋值给了x，并且打印出来,然后继续下一次循环停在yield处
# f.send('xiang') # x==xiang
# print(next(f)) # None没有给x赋值，执行print语句，打印出None,继续循环停在yield处


############################################################################
def deco(func):
    def wrapper():
        res = func()
        next(res)
        return res
    return wrapper


@deco
def func1():
    food_list = list()
    while True:
        x = yield food_list
        food_list.append(x)
        print('food_list==%s' % food_list)


f1 = func1()
f1.send('水蜜桃')
f1.send('榴莲')
f1.send('苹果')

# output
# food_list==['水蜜桃']
# food_list==['水蜜桃', '榴莲']
# food_list==['水蜜桃', '榴莲', '苹果']


