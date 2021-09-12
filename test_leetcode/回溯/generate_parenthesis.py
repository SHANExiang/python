

class Solution:

    # 暴力法
    def generate_parenthesis(self, n):
        res = []

        def valid(A):
            balance = 0
            for ch in A:
                if ch == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        def generate(A):
            if len(A) == 2*n:
                if valid(A):
                    res.append(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
        generate([])
        return res

    # 如果左括号数量不大于 nn，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号
    def generateParenthesis2(self, n: int):
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


    def generateParenthesis3(self, n: int):
        res = []
        cur_str = ''
        def dfs(cur_str, left, right):
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if left > right:
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)
        dfs(cur_str, n, n)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis2(4))
