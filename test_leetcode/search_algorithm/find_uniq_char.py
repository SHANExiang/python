

#

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return " "
        n = len(s)
        seen = set()
        for i in range(n):
            if s[i] in seen:
                continue
            seen.add(s[i])
            if s[i] not in s[i + 1:]:
                return s[i]
        return " "

    def firstUniqChar2(self, s: str) -> str:
        dic = dict()
        for ch in s:
            dic[ch] = not ch in dic
        for ch in s:
            if dic[ch]:
                return ch
        return " "

    def firstUniqChar3(self, s: str) -> str:
        dic = dict()
        for ch in s:
            dic[ch] = not ch in dic
        for ch in s:
            if dic[ch]:
                return ch
        return " "


if __name__ == "__main__":
    solution = Solution()
    print(solution.firstUniqChar("dgcsd"))
