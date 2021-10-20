

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.prev = ListNode(-1)
        self._count = 0

    def get(self, index: int) -> int:
        if 0 <= index < self._count:
            cur = self.prev
            for _ in range(index+1):
                 cur = cur.next
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index > self._count:
            return
        self._count += 1
        prev_node, cur = None, self.prev
        add_node = ListNode(val)
        for i in range(index+1):
            prev_node, cur = cur, cur.next
        prev_node.next, add_node.next = add_node, cur

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._count:
            self._count -= 1
            prev_node, cur = None, self.prev
            for i in range(index + 1):
                prev_node, cur = cur, cur.next
            prev_node.next, cur.next = cur.next, None


if __name__ == "__main__":
    obj = MyLinkedList()
    param_1 = obj.get(0)
    obj.addAtHead(2)
    obj.addAtTail(3)
    obj.addAtIndex(2, 3)
    obj.deleteAtIndex(3)

