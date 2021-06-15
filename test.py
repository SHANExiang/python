

class Solution:
    def maxSubArray(self, nums) -> int:
        n, i, j, max_sum, tmp = len(nums), 0, 1, nums[0], nums[0]
        if n == 1:
            return nums[0]
        for i in range(n):
            for j in range(i+1, n+1):
                tmp = sum(nums[i:j])
                if tmp > max_sum:
                    max_sum = tmp
        return max_sum


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2, 3, 2, 1, -5]))
