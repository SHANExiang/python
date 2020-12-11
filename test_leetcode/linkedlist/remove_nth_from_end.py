

"""
删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def remove_nth_from_end1(self, head, n):
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        dummy = ListNode(0, head)
        cur = dummy
        for x in range(1, get_length(head) - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    def remove_nth_from_end2_use_stack(self, head, n):
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        while cur:
            stack.append(cur.next)
            cur = cur.next
        for x in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next

    def remove_nth_from_end3(self, head, n):
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for x in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
