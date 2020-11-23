
"""
Write a Python program to create a singly linked list, append some items
and iterate through the list.
"""


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def iterate_item(self):
        current_item = self.tail
        while current_item:
            value = current_item.data
            current_item = current_item.next
            yield value

    def append_item(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

    def search_item(self, target):
        while self.tail:
            if target == self.tail.data:
                return True
            else:
                self.tail = self.tail.next
        return False

    def __getitem__(self, index):
        if index > self.count - 1:
            return 'Index out of range'
        current_value = self.tail
        for x in range(index):
            current_value = current_value.next
        return current_value.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception('index out of range')
        current = self.tail
        for x in range(index):
            current = current.next
        current.data = value

    def delete_item(self, item):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == item:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.count -= 1
            prev = current
            current = current.next


items = SinglyLinkedList()
items.append_item('python')
items.append_item('php')
items.append_item('c#')
items.append_item('c++')
items.append_item('java')
# for value in items.iterate_item():
#     print(value)
# print(items.count) # 5
# print(items.search_item("javascript"))  # False
# print(items[0])
# print(items[1])
# print(items[2])
# items[4] = 'dongxiang'
# print(items[4])

items.delete_item('python')
for value in items.iterate_item():
    print(value)
