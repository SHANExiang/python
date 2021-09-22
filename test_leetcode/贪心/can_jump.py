

#给定一个非负整数数组nums ，你最初位于数组的 第一个下标 。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个下标。


# 思路：尽可能到达最远位置（贪心）。
# 如果能到达某个位置，那一定能到达它前面的所有位置。
#
# 方法：初始化最远位置为 0，然后遍历数组，如果当前位置能到达，并且当前位置+跳数>最远位置，就更新最远位置。
# 最后比较最远位置和数组长度。


class Solution:
    def canJump(self, nums) :
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i+jump  #更新最远能到达位置
        return max_i>=i

    # 超时
    def canJump2(self, nums) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        i = 0
        while i < n:
            if not dp[i]:
                return False
            end = i + nums[i] + 1
            for j in range(i+1, end):
                if j < n:
                    dp[j] = True
            i = i + 1
        return dp[n-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump([1, 2, 0, 8]))
