import collections


"""
有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
"""


# 排序后相等即可
class Solution(object):
    def is_anagram(self, s, t):
        from collections import Counter
        return Counter(s) == Counter(t)

    def is_anagram2(self, s, t):
        from collections import defaultdict
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for ch in s:
            s_dict[ch] += 1
        for ch in t:
            t_dict[ch] += 1
        return s_dict == t_dict


if __name__ == "__main__":
    solution = Solution()
    print(solution.is_anagram('rat', 'car'))
