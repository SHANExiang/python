

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x//2+1
        while left <= right:
            mid = (right+left)//2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                right = mid-1
            else:
                left = mid + 1
        return right


if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(0))
