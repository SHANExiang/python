
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        if not s:
            return 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if len(set(s[i:j])) == j - i:
                    if j - i > max:
                        max = j - i
        return max

    def lengthOfLongestSubstring1(self, s: str) -> int:
        if not s:
            return 0
        max_len = 1
        i, j = 0, 1
        while i < j < len(s):
            if s[j] in s[i:j]:
                if max_len < j - i:
                    max_len = j - i
                i += 1
                j = i + 1
            else:
                j += 1
                if max_len < j - i:
                    max_len = j - i
        return max_len


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring1("abcabcbb"))

