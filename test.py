from collections import Counter


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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


if __name__ == "__main__":
    solution = Solution()
    node4 = ListNode(7)
    node3 = ListNode(7)
    node2 = ListNode(7)
    node1 = ListNode(7)
    head = ListNode(7)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print(solution.removeElements(head, 7))
