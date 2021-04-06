

# 给定两个字符串s和t，判断它们是否是同构的。
#
# 如果s中的字符可以按某种映射关系替换得到t，那么这两个字符串是同构的。
#
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。


class Solution:
    def isIsomorphic(self, s, t):
        dic = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
               'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16,
               'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
               'z': 25}
        res_set = set()
        for i in range(len(s)):
            if dic[s[i]] > dic[t[i]]:
                res_set.add(dic[t[i]] + 25 - dic[s[i]])
            else:
                res_set.add(dic[t[i]] - dic[s[i]])

        return len(res_set) == 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))
