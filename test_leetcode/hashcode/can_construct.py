

# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。
#
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)
#

# 输入：ransomNote = "aa", magazine = "aab"
# 输出：true


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        dic = defaultdict(int)
        for num in ransomNote:
            dic[num] += 1
        for num in  magazine:
            if num in dic:
                dic[num] -= 1
        for num, value in dic.items():
            if value > 0:
                return False
        return True

    def can_construct(self, ransomNote, magazine):
        import collections
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        x = c1 - c2
        if (len(x) == 0):
            return True
        else:
            return False
