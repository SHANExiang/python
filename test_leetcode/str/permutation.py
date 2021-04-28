
# 输入一个字符串，打印出该字符串中字符的所有排列。

# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

# 示例:
#
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]


class Solution:
    # 超时
    def permutation(self, s: str):
        from itertools import permutations
        res = []
        for ele in list(permutations(s)):
            permutation = "".join(ele)
            if permutation not in res:
                res.append(permutation)
        return res

    def permutation1(self, s):
        n, c, res = len(s), list(s), list()

        def dfs(x):
            if x == n:
                res.append(''.join(c))
                return
            seen = set()
            for i in range(x, n):
                if c[i] in seen:
                    continue
                seen.add(c[i])
                c[x], c[i] = c[i], c[x]
                dfs(x+1)
                c[x], c[i] = c[i], c[x]
        dfs(0)
        return res

    def permutation2(self, s):
        res = list()
        def dfs(s, path):
            if not s:
                res.append(path)
                return
            seen = set()
            for i in range(len(s)):
                if s[i] in seen:
                    continue
                seen.add(s[i])
                dfs(s[:i] + s[i+1:], path + s[i])
        dfs(s, '')
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.permutation2('abc'))
