

class Solution(object):
    @staticmethod
    def validity_string_parentheses1(original_string):
        original_list = list(original_string)
        pattern = {'{': '}', '[': ']', '(': ')'}
        while original_list:
            length = len(original_list)
            for i in range(0, len(original_list)):
                if original_list[i] == pattern[original_list[0]]:
                    original_list.remove(original_list[i])
                    original_list.remove(original_list[0])
                    break
            if len(original_list) == length:
                return False
        return True

    @staticmethod
    def validity_string_parentheses2(original_string):
        stack, pchar = [], {'(': ')', '[': ']', '{': '}'}
        for parenthese in original_string:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0


# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。




# solution = Solution()
# print(solution.validity_string_parentheses1("([)]"))
# print(solution.validity_string_parentheses2("({)[(}])(){}"))


class Solution1:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        nums_sum = sum(range(n+1))
        for i in nums:
            nums_sum -= i
        return nums_sum


if __name__ == "__main__":
    solution = Solution1()
    print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))