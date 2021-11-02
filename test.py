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
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(s):
            st = list(s)
            left, right = 0, len(s) - 1
            while left < right:
                st[left], st[right] = st[right], st[left]
                left += 1
                right -= 1
            return ''.join(st)

        cur, n = 0, len(s)
        res = ''
        while 2*k + cur <= n:
            res += reverse(s[cur:cur+k])
            res += s[cur+k:cur+2*k]
            cur = cur + 2*k
        if n - cur < k:
            res += reverse(s[cur:])
        if k <= n - cur < 2*k:
            res += reverse(s[cur:cur+k])
            res += s[cur+k:]
        return res

    def reverseStr2(self, s: str, k: int) -> str:
        """
        1. 使用range(start, end, step)来确定需要调换的初始位置
        2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
        3. 用切片整体替换，而不是一个个替换.
        """

        def reverse_substring(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text

        res = list(s)

        for cur in range(0, len(s), 2 * k):
            res[cur: cur + k] = reverse_substring(res[cur: cur + k])

        return ''.join(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseStr('abcdefg', 2))
