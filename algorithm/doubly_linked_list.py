

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

    def iterate_backward(self):
        current = self.tail
        while current:
            data = current.data
            current = current.prev
            yield data

    def print_backward1(self):
        for node in self.iterate_backward():
            print(node)

    def print_backward2(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

    def reversed(self):
        current = self.head
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = current.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp

    def insert_item_in_front_of_linked_list(self, item):
        if self.head is not None:
            node = Node(item, None, None)
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.count += 1

    def search_item(self, item):
        flag = False
        current = self.head
        while current and not flag:
            if current.data == item:
                flag = True
            else:
                current = current.next
        return flag

    def delete_item(self, item):
        current = self.head
        while current:
            if current == self.head and item == self.head.data:
                self.head = self.head.next
                self.head.prev = None
                break
            elif current == self.tail and item == self.tail.data:
                self.tail = self.tail.prev
                self.tail.next = None
                break
            elif current.data == item:
                current.prev.next = current.next
                current.next.prev = current.prev
                break
            else:
                current = current.next
        self.count -= 1


d = DubbleLinkedList()
d.append_item('python')
d.append_item('c++')
d.append_item('java')
d.append_item('javascript')
d.append_item('php')

# 向前迭代
# d.print_forward()
# python
# c++
# java
# javascript
# php

# 向后迭代
# d.print_backward1()
# php
# javascript
# java
# c++
# python

# d.print_backward2()
# php
# javascript
# java
# c++
# python

# 双向链表的节点个数
# print(d.count)
# 5

# d.reversed()
# d.print_forward()
# php
# javascript
# java
# c++
# python

# 在head之前插入一个元素
# d.print_forward()
# python
# c++
# java
# javascript
# php

# d.insert_item_in_front_of_linked_list('go')
# d.print_forward()
# go
# python
# c++
# java
# javascript
# php

# print(d.search_item('go')) # False
# print(d.search_item('java')) # True

d.delete_item('c++')
d.print_forward()
# python
# java
# javascript
# php
