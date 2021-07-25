# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#
# 换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
#
#  
#
# 示例 1：
#
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
# 示例 2：
#
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False


class Solution:
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        n = len(s1)
        strs = list(s1)
        seen = [False for _ in range(n)]
        path, depth, res = [], 0, []

        def dfs(strs, depth, seen, path, res):
            if n == depth:
                res.append(path[:])
                return
            for i, used in enumerate(seen):
                if used:
                    continue
                path.append(strs[i])
                seen[i] = True
                dfs(strs, depth+1, seen, path, res)
                path.pop()
                seen[i] = False
        dfs(strs, depth, seen, path, res)
        res = [''.join(x) for x in res]
        print(res)
        for s in res:
            if s in s2:
                return True
        return False

    def check_inclusion2(self, s1, s2):
        for index, s in enumerate(s2):
            lis = list(s1)
            if s in lis:
                i, j = index, index+1
                lis.remove(s)
                if not lis:
                    return True
                while j < len(s2):
                    if s2[j] in lis:
                        lis.remove(s2[j])
                        j += 1
                        if not lis:
                            return True
                    else:
                        if not lis:
                            return True
                        break
            else:
                continue
        return False

    def check_inclusion3(self, s1, s2):
        from collections import Counter
        return any([Counter(s1) == Counter(s2[i:i+len(s1)]) for i in range(len(s2) - len(s1) + 1)])


if __name__ == "__main__":
    solution = Solution()
    print(solution.check_inclusion3("a", "ab"))

