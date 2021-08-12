from collections import Counter

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        n, res = len(strs), ''
        if n == 1:
            return strs[0]
        n_min = min([len(str) for str in strs])
        if n_min == 0:
            return ''
        i = 0
        while i < n_min:
            if all([str[i] == strs[0][i] for str in strs]):
                res += strs[0][i]
                i += 1
            else:
                break
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["dog","racecar","car"]))
