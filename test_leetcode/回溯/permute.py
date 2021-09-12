

# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 示例 3：
#
# 输入：nums = [1]
# 输出：[[1]]


class Solution:
    def permute(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for index, ele in enumerate(nums):
            res.extend([ele]+ p for p in self.permute(nums[0:index]+nums[index+1:]))
        return res

    def permute2(self, nums):
        def backtrack(nums, depth, used_list, path, res):
            if depth == len(nums):
                res.append(path[:])
                return
            for index, used in enumerate(used_list):
                if used:
                    continue
                path.append(nums[index])
                used_list[index] = True
                backtrack(nums, depth+1, used_list, path, res)
                path.pop()
                used_list[index] = False
        used_list = [False for _ in nums]
        depth, path, res = 0, [], []
        backtrack(nums, depth, used_list, path, res)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1, 2, 3]))