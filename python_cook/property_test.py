

class Person(object):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('not str value')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('attribute name not be deleted.')


class SubPerson(Person):
    @property
    def name(self):
        print('get person name')
        return super().name

    @name.setter
    def name(self, value):
        print('set name value', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('delete name')
        super(SubPerson, SubPerson).name.__delete__(self)


if __name__ == "__main__":
    # person = Person('dong')
    # print(person.name)
    # person.name = 'xiang'
    # print(person.name)
    # del person.name

    subperson = SubPerson('dong')
    print(subperson.name)
    subperson.name = 'xiang'
    print(subperson.name)
    del subperson.name
