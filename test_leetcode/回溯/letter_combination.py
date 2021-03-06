

# 17. 电话号码的字母组合
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


class Solution:
    def letterCombinations(self, digits: str):
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []
        n = len(digits)
        if n == 1:
            return mappings[digits]
        res = []
        combination = []
        def backtrack(index):
            if index == n:
                res.append("".join(combination))
                return
            else:
                mapping = mappings[digits[index]]
                for st in mapping:
                    combination.append(st)
                    backtrack(index+1)
                    combination.pop()
        backtrack(0)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations('234'))
