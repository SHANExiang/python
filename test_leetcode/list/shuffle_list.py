

# 384. 打乱数组
# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
#
# 实现 Solution class:
#
# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果
#
#
# 示例：
#
# 输入
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# 输出
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
#
# 解释
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
# solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
# solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        import random
        n = len(self.nums)
        random_int = random.randint(0, n-1)
        permute_list = []
        used_list = [False for _ in range(n)]
        depth, path = 0, []
        def backtrace(nums, depth, used_list, path, permute_list):
            if depth == len(nums):
                permute_list.append(path[:])
                return
            for i, used in enumerate(used_list):
                if used:
                    continue
                path.append(nums[i])
                used_list[i] = True
                backtrace(nums, depth+1, used_list, path, permute_list)
                path.pop()
                used_list[i] = False
        backtrace(self.nums, depth, used_list, path, permute_list)
        return permute_list[random_int]


if __name__ == "__main__":
    solution = Solution([1,2,3])
    print(solution.shuffle())