

def spam():
    print('spam')


def test(*args, **kwargs):
    print('test')


bar = 'dong'


# 表示只有此列表中的属性可以被其它模块导出
__all__ = ['spam', 'bar']
