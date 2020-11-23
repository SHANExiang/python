

class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DubbleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def iterate_item(self):
        current = self.head
        while current:
            data = current.data
            current = current.next
            yield data

    def append_item(self, item):
        new_item = Node(item, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1

    def print_forward(self):
        for node in self.iterate_item():
            print(node)


d = DubbleLinkedList()
d.append_item('python')
d.append_item('c++')
d.append_item('java')
d.append_item('javascript')
d.append_item('php')

d.print_forward()
