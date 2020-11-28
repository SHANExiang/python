

# 给定两个数组，编写一个函数来计算它们的交集。


class Solution:
    def intersect(self, nums1, nums2):
        result = list()
        for x in nums1:
            if x in nums2:
                nums2.remove(x)
                result.append(x)
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.intersect([1, 2, 2, 2, 1], [2, 2]))
    print(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
