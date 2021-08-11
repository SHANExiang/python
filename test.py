from collections import Counter


class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1
        while left < right:
            if not s[left].isdigit() and not s[left].isalpha():
                left += 1
            elif not s[right].isdigit() and not s[right].isalpha():
                right -= 1
            else:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("Aman, n plan, a canal: Panama"))
