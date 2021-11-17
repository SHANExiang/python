

# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
#


class Solution:
    def topKFrequent(self, nums, k: int):
        from collections import Counter
        c = Counter(nums)
        return [item[0] for item in c.most_common(k)]

    def top_k_frequent(self, nums, k):
        dic = dict()
        for num in nums:
            if num in dic:
                dic[nums] += 1
            else:
                dic[num] = 1
        queue = list()
        import heapq
        for key, value in dic.items():
            heapq.heappush(queue, (value, key))
            if len(queue) > k:
                heapq.heappop(queue)
        result = [0] * k
        for i in range(k - 1, 1, -1):
            result[i] = heapq.heappop(queue)[1]
        return result

