

#


class NestedIterator:
    def __init__(self, nestedList):
        self.nestedList = nestedList
        self.output = list()

        def recur(lis, output):
            for l in lis:
                if isinstance(l, list):
                    recur(l, output)
                else:
                    output.append(l)

        recur(self.nestedList, self.output)

    def next(self) -> int:
        if not self.hasNext:
            return
        else:
            return self.output.pop(0)

    def hasNext(self) -> bool:
        if not self.output:
            return False
        else:
            return True


if __name__ == "__main__":
    nested_list = NestedIterator([[1,1],2,[1,1]])
    print(nested_list.next())
    print(nested_list.next())
    print(nested_list.next())
    print(nested_list.next())
    print(nested_list.next())
    print(nested_list.next())

