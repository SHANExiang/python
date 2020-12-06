

"""
外观数列
给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：
countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
"""


class Solution(object):
    def count_and_say(self, n):
        if n == 1:
            return '1'
        else:
            origin_str = self.count_and_say(n - 1)
            if len(origin_str) == 1:
                return '11'
            left = 0
            right = left + 1
            result = str()
            while right < len(origin_str):
                if origin_str[right] == origin_str[left]:
                    right += 1
                    if right >= len(origin_str):
                        count = right - left
                        result += '%s%s' % (count, origin_str[left])
                else:
                    count = right - left
                    result += '%s%s' % (count, origin_str[left])
                    left = right
                    right = left + 1
                    if right >= len(origin_str):
                        count = right - left
                        result += '%s%s' % (count, origin_str[left])
            return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.count_and_say(2))  # 13112221





