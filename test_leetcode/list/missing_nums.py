
# 给定一个包含 [0, n]中n个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
#
# 进阶：
#
# 你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
#


class Solution:
    # math
    def missingNumber(self, nums) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

    # 哈希表
    def missingNumber2(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

    # 位运算
    def missingNumber3(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    # 排序
    def missing_number4(self, nums):
        nums.sort()
        for index, num in enumerate(nums):
            if index != num:
                return index
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.missing_number4([9,6,4,2,3,5,7,0,1]))
    print(solution.missing_number4([3,0,1]))
    print(solution.missing_number4([0,1]))
