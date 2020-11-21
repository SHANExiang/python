"""
Write a Python program to get all possible unique subsets from a set of distinct integers.
"""


class Solution(object):
    def get_subset(self, subset):
        return self.subset_recur([], sorted(subset))

    def subset_recur(self, current, subset):
        if subset:
            return self.subset_recur(current, subset[1:]) + \
                   self.subset_recur(current + [subset[0]], subset[1:])
        return [current]


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(1000)
    solution = Solution()
    print(solution.get_subset([3, 4, 5]))
