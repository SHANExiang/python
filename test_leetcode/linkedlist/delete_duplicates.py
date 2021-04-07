

# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
#
# 返回同样按升序排列的结果链表。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


if __name__ == "__main__":
    solution = Solution()
    node3 = ListNode(2, None)
    node2 = ListNode(1, node3)
    node1 = ListNode(1, node2)
    head = ListNode(1, node1)
    res = solution.deleteDuplicates(head)
    while res:
        print(res.val)
        res = res.next

