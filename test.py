

# [1,  2, 3,  4]
# [5,  6, 7,  8]
# [9, 10, 11, 12]

class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count, start, origin = 0, 0, nums[0]
        while count < n:
            if start + k <= n - 1:
                next = start + k
            else:
                next = (start + k) % n
            origin, nums[next] = nums[next], origin
            start = next
            count += 1
        print(nums)


if __name__ == "__main__":
    solution = Solution()
    print(solution.rotate([1,2,3,4,5,6,7], 3))
    print(solution.rotate([-1,-100,3,99], 2))
