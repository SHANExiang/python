import re


# 定义了__get__,__set__,__delete__中的任意一个方法的对象都叫描述符
# 一个在初始化对象的时候判定email是否合法
class Person(object):
    def __init__(self, email):
        m = re.match('\w+@\w+\.\w+', email)
        if not m:
            raise Exception('email not valid')
        self.email = email


# 执行代码
# p = Person('efeg23@126.com')
# print(p.email)
# p.email = 'gdfgft@163.com'
# print(p.email)
# # p1 = Person('gtjyhergrt')    # Exception: email not vaild
# p.email = 'dgfhgth'
# print(p.email)  # dgfhgth
# 正常打印，说明当给对象属性进行赋值时，并不能调用email合法性校验，所以引入描述符
# 对于实例a，a.x的查找顺序为a.__dict__['x'],然后是type(a).__dict__['x'].
# 如果还是没找到就往上级(父类)中查找。


# 基于类创建描述符
class Email(object):
    def __init__(self):
        self._name = ''

    def __get__(self, instance, owner):
        return self._name

    def __set__(self, instance, value):
        m = re.match('\w+@\w+\.\w+', value)
        if not m:
            raise Exception('email not valid')
        self._name = value

    def __delete__(self, instance):
        del self._name


class Person1(object):
    email = Email()


# 执行代码
# p2 = Person1()
# p2.email = '234354@126.com'
# print(p2.email) # print(p2.email) #
# p2.email = 'sfgdgfrgr' # Exception: email not valid


# 使用property函数创建描述符
class Person2(object):
    def __init__(self):
        self._email = None

    def get_email(self):
        return self._email

    def set_email(self, email):
        m = re.match('\w+@\w+\.\w+', email)
        if not m:
            raise Exception('email not valid')
        self._email = email

    def delete_email(self):
        del self._email

    email = property(get_email, set_email, delete_email, 'email valid check')


# 执行代码
# p3 = Person2()
# p3.email = '234354@126.com'
# print(p3.email) # 234354@126.com
# p3.email = 'sfgdgfrgr' # Exception: email not valid


class Person3(object):
    def __init__(self):
        self._email = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        m = re.match('\w+@\w+\.\w+', email)
        if not m:
            raise Exception('email not valid')
        self._email = email

    @email.deleter
    def email(self):
        del self._email


p4 = Person3()
p4.email = 'dgfgrhtyjy@163.com'
print(p4.email)
p4.email = 'grfghoosf' # Exception: email not valid
