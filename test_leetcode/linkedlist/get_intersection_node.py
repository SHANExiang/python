

# 输入两个链表，找出它们的第一个公共节点。
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_A, len_B = 0, 0
        cur_A, cur_B = headA, headB
        while cur_A:
            len_A += 1
            cur_A = cur_A.next
        while cur_B:
            len_B += 1
            cur_B = cur_B.next
        if len_B >= 1 and len_A >= 1:
            diff = len_A - len_B
            if diff == 0:
                cur_A, cur_B = headA, headB
            elif diff > 0:
                while diff > 0:
                    cur_A = headA.next
                    headA = headA.next
                    diff -= 1
                cur_B = headB
            else:
                while diff < 0:
                    cur_B = headB.next
                    headB = headB.next
                    diff += 1
                cur_A = headA
            while cur_A:
                if cur_A is cur_B:
                    return cur_A
                cur_A = cur_A.next
                cur_B = cur_B.next
        return None
