

"""
实现 strStr()
实现strStr()函数。

给定一个haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回 -1。
示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1
"""


class Solution(object):
    def str_str(self, haystack, needle):
        if not needle:
            return 0
        i, n = 0, len(needle)
        while i + n <= len(haystack):
            if needle == haystack[i:i + n]:
                return i
            i += 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.str_str('ggjaaagfg', 'aaa'))
