

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index in range(len(s)):
            if s[index] not in s[index + 1:] and s[index] not in s[0:index]:
                return index
        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.firstUniqChar("ab"))
