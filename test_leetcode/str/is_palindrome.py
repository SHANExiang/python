

"""
验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:
输入: "race a car"
输出: false
"""


class Solution(object):
    def is_palindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalpha() and not s[left].isdigit():
                left += 1
                continue
            if not s[right].isalpha() and not s[right].isdigit():
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True

    def is_palindrome2(self, s):
        import re
        result_list = re.findall("[A-Za-z0-9]", s, re.IGNORECASE)
        print(result_list)
        result_list = [str(ele).lower() for ele in result_list]
        return result_list == result_list[::-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.is_palindrome("A man, a plan, a canal: Panama"))
    print(solution.is_palindrome("race a car"))
