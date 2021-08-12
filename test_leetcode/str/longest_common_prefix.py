

"""
最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"
示例2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
"""


class Solution(object):
    def longest_common_prefix(self, strs):
        # strs = ["flower","flow","flight"]
        # list(zip(*strs))
        # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]

        res_str = ''
        for x in zip(*strs):
            tmp_set = set(x)
            if len(tmp_set) == 1:
                res_str += x[0]
            else:
                break
        return res_str

    def longestCommonPrefix2(self, strs) -> str:
        n, res = len(strs), ''
        if n == 1:
            return strs[0]
        n_min = min([len(str) for str in strs])
        if n_min == 0:
            return ''
        i = 0
        while i < n_min:
            if all([str[i] == strs[0][i] for str in strs]):
                res += strs[0][i]
                i += 1
            else:
                break
        return res

    # 按字典排序数组，比较第一个，和最后一个单词，有多少前缀相同。
    def longestCommonPrefix3(self, s) -> str:
        if not s:
            return ""
        s.sort()
        n = len(s)
        a = s[0]
        b = s[n - 1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res




if __name__ == '__main__':
    solution = Solution()
    print(solution.longest_common_prefix(["flower", "flow", "flight"]))
    print(solution.longest_common_prefix(["dog", "racecar", "car"]))
    print(solution.longest_common_prefix([]))
    print(solution.longest_common_prefix(['ab', 'a']))

