
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def has_cycle1(self, head: ListNode) -> bool:
        seen = set()
        while True:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

    def has_cycle2(self, head):
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
