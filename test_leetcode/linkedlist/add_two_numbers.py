

# 给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0开头。
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        l1_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
        l2_list = []
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        l1_sum = 0
        for i in range(len(l1_list) - 1, -1, -1):
            l1_sum += l1_list[len(l1_list)-i-1]* pow(10, i)
        l2_sum = 0
        for i in range(len(l2_list) - 1, -1, -1):
            l2_sum += l2_list[len(l2_list)-i-1]* pow(10, i)
        sum_two = l1_sum + l2_sum
        value = sum_two % 10
        sum_two = sum_two // 10
        head = ListNode(value)
        dumy = head
        while sum_two > 0:
            num = sum_two % 10
            head.next = ListNode(num)
            head = head.next
            sum_two //= 10
        return dumy

    def addTwoNumbers2(self, l1, l2):
        pre = cur = ListNode(0)
        carry = 0
        while l1 or l2:
            if not l1:
                sum_two = l2.val + carry
                value = sum_two % 10
                carry = sum_two // 10
                Node = ListNode(value)
                l2 = l2.next
            elif not l2:
                sum_two = l1.val + carry
                value = sum_two % 10
                carry = sum_two // 10
                Node = ListNode(value)
                l1 = l1.next
            else:
                sum_two = l1.val + l2.val + carry
                value = sum_two % 10
                carry = sum_two // 10
                Node = ListNode(value)
                l1 = l1.next
                l2 = l2.next
            cur.next = Node
            cur = cur.nxxt
        if carry == 1:
            Node = ListNode(1)
            cur.next = Node
        return pre.next
