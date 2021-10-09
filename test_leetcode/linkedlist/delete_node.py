

"""
删除链表中的节点
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


head_list = [4, 5, 6, 8]


class Solution:
    def delete_node(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.next = node.next.next
        node.val = node.next.val


# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
# 返回删除后的链表的头节点。


# 示例 1:
#
# 输入: head = [4,5,1,9], val = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.


class Solution1:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pre = ListNode(-1)
        pre.next = head
        dumy = pre
        while head:
            if val == head.val:
                pre.next = head.next
                if head.next:
                    pre.next.val = head.next.val
            head = head.next
            pre = pre.next
        return dumy.next

    def delete_node2(self, head, val):
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur:
            pre.next = cur.next
        return head

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur = ListNode(0)
        cur.next = head
        pre = cur
        while cur:
            if cur.next and val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return pre.next


if __name__ == '__main__':
    node = ListNode(2)
    solution = Solution()
    solution.delete_node(node)
