

class Foo(object):
    def get_bar(self):
        return 'dong is a genius'

    BAR = property(get_bar)


# 执行结果
# obj = Foo()
# print(obj.get_bar())   # dong is a genius
# result = obj.BAR
# print(result) # dong is a genius


class Foo1(object):
    def get_bar(self):
        return 'dong is a genius'

    def set_bar(self, name):
        return '%s is a genius, yes, you are right.' % name

    def del_bar(self):
        return 'dong is a foolish man'

    BAR = property(get_bar, set_bar, del_bar, 'description dong...')


# 执行结果
# foo = Foo1()
# print(foo.BAR)  # 自动调用第一个参数中定义的方法：get_bar
# foo.BAR = 'shane'  # 自动调用第二个参数中定义的方法：set_bar方法，并将“shane”当作参数传入
# print(foo.BAR)
# del foo.BAR  # 自动调用第三个参数中定义的方法：del_bar方法
# print(foo.BAR.__doc__)  # 自动获取第四个参数中设置的值：description dong...

print(__name__)