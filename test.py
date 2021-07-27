class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for index, ch in enumerate(s):
            seen = []
            seen.append(ch)
            right = index + 1
            while right < len(s):
                if s[right] in seen:
                    break
                else:
                    seen.append(s[right])
                    right += 1
            max_len = max(max_len, right - index)
        return max_len



if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring('pwwkew'))
