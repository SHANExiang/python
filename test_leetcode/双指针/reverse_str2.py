

# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
#
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。


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
