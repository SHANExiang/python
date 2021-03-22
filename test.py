

class A(object):
    def show(self):
        print('A detail')


class B(A):
    def show(self):
        print('B detail')


obj = B()
obj.__class__ = A
obj.show()
