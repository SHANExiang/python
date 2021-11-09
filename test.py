from collections import Counter, defaultdict


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
    def isValid(self, s: str) -> bool:
        map = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if not stack and ch in map:
                return False
            if ch in map.values():
                stack.append(ch)
            else:
                if map.get(ch) == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid('(})'))
