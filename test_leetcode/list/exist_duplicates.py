

class Solution(object):
    """
    给定一个整数数组，判断是否存在重复元素。
    如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
    """

    def contains_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(list(set(nums))) != len(nums) else False


if __name__ == "__main__":
    solution = Solution()
    print(solution.contains_duplicate([1, 2, 3, 1]))
