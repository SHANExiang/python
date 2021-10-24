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
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            tmp = 0
            while n > 0:
                a = n % 10
                tmp += a * a
                n //= 10
            n = tmp
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(2))
