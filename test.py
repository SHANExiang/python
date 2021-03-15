

class Person(object):
    def foo(self, num):
        print('foo %s' % num)

    @staticmethod
    def foo_static(num):
        print('foo_static %s' % num)

    @classmethod
    def foo_cls(cls, num):
        print('foo_cls %s' % num)


if __name__ == "__main__":
    person = Person()
    person.foo(1)
    # Person.foo(2)
    person.foo_cls(2)
    Person.foo_cls(2)
    person.foo_static(3)
    Person.foo_static(3)