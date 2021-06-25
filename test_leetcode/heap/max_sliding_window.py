

# 239. 滑动窗口最大值
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# 示例 2：
#
# 输入：nums = [1], k = 1
# 输出：[1]
# 示例 3：
#
# 输入：nums = [1,-1], k = 1
# 输出：[1,-1]
# 示例 4：
#
# 输入：nums = [9,11], k = 2
# 输出：[11]
# 示例 5：
#
# 输入：nums = [4,-2], k = 2
# 输出：[4]
#
#
# 提示：
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

import heapq


class Solution:
    # 优先队列--python中的最小堆heapq
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        res = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while i - k >= q[0][1]:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res

    def max_sliding_window(self, nums, k):
        n = len(nums)
        from collections import deque
        q = deque()
        for i in range(0, k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        res = []
        res.append(nums[q[0]])
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            res.append(nums[q[0]])
        return res

    def max_sliding_window2(self, nums, k):
        from collections import deque
        n = len(nums)
        d, res = deque(), []
        for i, j in zip(range(1-k, n+1-k), range(n)):
            if i > 0 and d[0] == nums[i - 1]:
                d.popleft()
                # 保持 deque 递减
            while d and d[-1] < nums[j]:
                d.pop()
            d.append(nums[j])
            # 记录窗口最大值
            if i >= 0:
                res.append(d[0])
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.max_sliding_window2([9,10,9,-7,-4,-8,2,-6], 5))

