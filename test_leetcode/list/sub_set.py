

# 78. 子集
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
# 提示：
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同


class Solution:
    def subsets(self, nums):
        n = len(nums)
        if n == 1:
            return [[], [nums[0]]]
        tmp = self.subsets(nums[1:])
        import copy
        res = copy.deepcopy(tmp)
        for ele in tmp:
            ele.append(nums[0])
            res.append(ele)
        return res

    def sub_sets1(self, nums):
        res = [[]]
        for i in nums:
            res += [[i] + num for num in res]
        return res

    # BFS 实际同sub_sets1
    def sub_sets2(self, nums):
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                res.append(res[j]+[nums[i]])
        return res

    # 回溯
    def sub_sets3(self, nums):
        self.res = []
        path, n = [], len(nums)
        def backtrack(startindex):
            self.res.append(path[:])
            if startindex >= n:
                return
            for i in range(startindex, n):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return self.res


if __name__ == "__main__":
    solution = Solution()
    print(solution.sub_sets3([1,2,3]))
