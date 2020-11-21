

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


solution = Solution()
# print(solution.validity_string_parentheses1("({)[(}])(){}"))
print(solution.validity_string_parentheses2("({)[(}])(){}"))
