from collections import Counter, defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MyQueue(object):
    def __init__(self):
        self.queue = []

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)

    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        queue = MyQueue()
        res, n = list(), len(nums)
        for i in range(0, k):
            queue.push(nums[i])
        res.append(queue.front())
        for i in range(k, n):
            queue.pop(nums[i-k])
            queue.push(nums[i])
            res.append(queue.front())
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4))
    l = sorted(dict(Counter([-7,-8,7,5,7,1,6,0])).items(), key=lambda x: x[0])