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

    def oddEvenList(self, head: ListNode) -> ListNode:
        pre = cur = ListNode(0)
        tmp = head
        while tmp:
            cur.next = head
            cur = cur.next
            if tmp.next:
                tmp = tmp.next.next
            else:
                break
        head = head.next
        while head:
            cur.next = head
            cur = cur.next
            if head.next:
                head = head.next.next
            else:
                break
        return pre.next


if __name__ == "__main__":
    solution = Solution()
