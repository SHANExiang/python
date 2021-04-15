

class LinkedList(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse_linkedlist1(self, head):
        prev = None
        cur = head
        while cur:
            node = cur.next
            cur.next = prev
            prev = cur
            cur = node
        return prev

    def reverse_linkedlist2(self, head):
        if head == None or head.next == None:
            return head
        node = self.reverse_linkedlist2(head.next)
        head.next.next = head
        head.next = None
        return node
