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


# 生成器就是个迭代器，有__iter__和__next__属性
print(hasattr(func(), '__next__')) # True
print(hasattr(func(), '__iter__')) # True


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


gen1 = grep(tail('test.txt'), 'error') # 动态跟踪文件新添加的内容,并且过滤出有patterns的行
gen2 = grep(gen1, '404')  # gen1为生成器

for x in gen2:   # 通过for循环来隐式调用__next__()方法
    print(x)
