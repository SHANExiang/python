

# 给你一个由 n 个整数组成的数组nums ，和一个目标值 target。
# 请你找出并返回满足下述全部条件且不重复的四元组[nums[a], nums[b], nums[c], nums[d]]
# （若两个四元组元素一一对应，则认为两个四元组重复）：
#
# 0 <= a, b, c, d< n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。
#


class Solution:
    # 双指针法
    def fourSum(self, nums, target: int):
        n, res = len(nums), []
        if n < 4:
            return []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j-1]: continue
                left = j + 1
                right = n - 1
                while left < right:
                    if nums[left] + nums[right] == target -nums[i] - nums[j]:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] > target -nums[i] - nums[j]: right -= 1
                    else: left += 1
        return res

    # hash法
    def four_sum(self, nums, target):
        n, res = len(nums), set()
        hashmap = dict()
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    val = target - nums[i] - nums[j] - nums[k]
                    if val in hashmap:
                        count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                        if hashmap[val] > count:
                            res.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
                    else: continue
        return res


if __name__ == "__main__":
    solution = Solution()
    # print(solution.fourSum([1,0,-1,0,-2,2], 0))
    print(solution.four_sum([1,0,-1,0,-2,2], 0))





