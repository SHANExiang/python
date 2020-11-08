import bisect
import collections.abc


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, item):
        return self._items[item]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)

# ****************************************************************************


class Item(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    def __getitem__(self, item):
        print('Getting:', item)
        return self._items[item]

    def __setitem__(self, key, value):
        print('Setting:', key, value)
        self._items[key] = value

    def __delitem__(self, key):
        print('Deleting:', key)
        del self._items[key]

    def insert(self, key, value):
        print('Inserting:', key)
        self._items.insert(key, value)

    def __len__(self):
        print('len')
        return len(self._items)


if __name__ == '__main__':
    # lis = [1, 2, 5]
    # bisect.insort(lis, 4)
    # print(lis)

    # sorted_items = SortedItems([67, 23, 24, 16, 56])
    # print(list(sorted_items))
    # sorted_items.add(73)
    # print(sorted_items[-2], sorted_items[3])
    # print(list(sorted_items))

    items = Item([2, 4, 5, 1])
    print(len(items))
    items.append(10)
    print(items.count(3))
    items.remove(4)
