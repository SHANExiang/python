

# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
#
# 示例 1:
#
# 输入: [7,5,6,4]
# 输出: 5
# 7, 5
# 7, 6
# 7, 4
# 5, 4
# 6, 4

class Solution:
    def reversePairs(self, nums) -> int:
        def count_smaller(num, dest):
            count, i = 0, 0
            while i < len(dest):
                if dest[i] < num:
                    count += 1
                i += 1
            return count
        res = 0
        for i in range(len(nums) - 1) :
            res += count_smaller(nums[i], nums[i+1:])
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.reversePairs([7,5,6,4]))

