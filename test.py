# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_tmp = ListNode(-1)
        pre = pre_tmp
        cur1, cur2 = l1, l2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                pre_tmp.next = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                pre_tmp.next = ListNode(cur2.val)
                cur2 = cur2.next
            pre_tmp = pre_tmp.next
        if cur1:
            pre_tmp.next = cur1
        if cur2:
            pre_tmp.next = cur2
        return pre.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    solution = Solution()
    solution.mergeTwoLists(l1, l2)
