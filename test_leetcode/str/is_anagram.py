import collections


"""
有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
"""


# 排序后相等即可
class Solution(object):
    def is_anagram(self, s, t):
        if len(s) != len(t):
            return False
        s = collections.Counter(s)
        t = collections.Counter(t)
        if s == t:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.is_anagram('rat', 'car'))
