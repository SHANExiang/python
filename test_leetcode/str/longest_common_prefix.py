

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
        res_str = ''
        for x in zip(*strs):
            tmp_set = set(x)
            if len(tmp_set) == 1:
                res_str += x[0]
            else:
                break
        return res_str



if __name__ == '__main__':
    solution = Solution()
    print(solution.longest_common_prefix(["flower", "flow", "flight"]))
    print(solution.longest_common_prefix(["dog", "racecar", "car"]))
    print(solution.longest_common_prefix([]))
    print(solution.longest_common_prefix(['ab', 'a']))

