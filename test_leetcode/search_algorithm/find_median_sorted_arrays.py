

# 4. 寻找两个正序数组的中位数
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 示例 2：
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
# 示例 3：
#
# 输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
# 示例 4：
#
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
# 示例 5：
#
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def get_middle_num(nums):
            if not nums:
                return 0
            n = len(nums)
            if n % 2 == 0:
                return (nums[n//2-1] + nums[n//2])/2
            else:
                return nums[n//2]

        m, n = len(nums1), len(nums2)
        if not nums1:
            return get_middle_num(nums2)
        if not nums2:
            return get_middle_num(nums1)
        res_list = []
        index1, index2 = 0, 0
        while index1 < m and index2 < n:
            if nums1[index1] > nums2[index2]:
                res_list.append(nums2[index2])
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                res_list.append(nums1[index1])
                index1 += 1
            else:
                res_list.append(nums1[index1])
                res_list.append(nums2[index2])
                index1 += 1
                index2 += 1
            if index1 == m:
                res_list.extend(nums2[index2:])
            if index2 == n:
                res_list.extend(nums1[index1:])
        print(res_list)
        return get_middle_num(res_list)



if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 2], [1, 3, 4]))




