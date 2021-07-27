
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

    def lengthOfLongestSubstring2(self, s: str) -> int:
        max_len = 0
        for index, ch in enumerate(s):
            seen = []
            seen.append(ch)
            right = index + 1
            while right < len(s):
                if s[right] in seen:
                    break
                else:
                    seen.append(s[right])
                    right += 1
            max_len = max(max_len, right - index)
        return max_len

    def length_of_longest_substring(self, s):
        n = len(s)
        res, tmp = 0, 0
        dic = dict()
        for i in range(n):
            old_index = dic.get(s[i], -1)
            dic[s[i]] = i
            tmp = tmp + 1 if tmp < i - old_index else i - old_index
            res = max(res, tmp)
        return res

    def length_of_longest_substring2(self, s):
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)  # 更新左指针 i
            dic[s[j]] = j  # 哈希表记录
            res = max(res, j - i)  # 更新结果
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.length_of_longest_substring2("abcabcbb"))

