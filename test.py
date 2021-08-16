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
    def romanToInt(self, s: str) -> int:
        map = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50,
               'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        left, n = 0, len(s)
        res = 0
        while left <= n - 1:
            if left + 1 < n:
                if s[left:left+2] in map:
                    res += map[s[left:left+2]]
                    left += 2
                    continue
            if s[left] in map:
                res += map[s[left]]
                left += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt('III'))
