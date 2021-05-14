

import contextlib


class Solution:
    def lengthOfLongestSubstring(self, s: str):
        res = 0
        for i in range(len(s)):
            seen = set()
            j = i
            while j < len(s):
                if s[j] not in seen:
                    seen.add(s[j])
                    j += 1
                    count = j - i
                    if count > res:
                        res = count
                else:
                    break
        return res




if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("ddd"))
