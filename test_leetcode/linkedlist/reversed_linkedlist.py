

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

    def reverse_linkedlist3(self, head):
        def recur(cur, pre):
            if not cur:
                return pre
            res = recur(cur.next, cur)
            cur.next = pre
            return res
        return recur(head, None)

    def reverse_linkedlist4(self, head):
        if not head:
            return None
        if head.next is None:
            return head
        node = self.reverse_linkedlist4(head.next)
        cur = node
        while cur:
            if cur.next is None:
                cur.next = head
                head.next = None
            cur = cur.next
        return node
