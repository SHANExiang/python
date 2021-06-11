

# 给你一个字符串 s，找到 s 中最长的回文子串。
# 示例 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
#
# 输入：s = "cbbd"
# 输出："bb"
# 示例 3：
#
# 输入：s = "a"
# 输出："a"
# 示例 4：
#
# 输入：s = "ac"
# 输出："a"
# 提示：
#
# 1 <= s.length <= 1000
# s 仅由数字和英文字母（大写和/或小写）组成


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j]表示从i到j组成的串是否是回文串
        if not s:
            return ""
        begin, n, max_len = 0, len(s), 1
        if n < 2:
            return s
        dp = [[False]*n for _ in range(n)]
        for index in range(n):
            dp[index][index] = True
        for j in range(1, n):
            for i in range(0, j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if max_len < j - i + 1 and dp[i][j]:
                    begin = i
                    max_len = j - i + 1
        return s[begin:begin+max_len]

    def longest_palindrome(self, s):
        n, max_len, res = len(s), 1, ''
        def expand(left, right):
            nonlocal res
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            res = s[left+1:right] if right - left - 1 > len(res) else res
        for index in range(n):
            expand(index, index)
            expand(index, index+1)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.longest_palindrome("cccc"))

