

# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于⌊ n/2 ⌋的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。


class Solution:
    def majorityElement(self, nums) -> int:
        beyond_counter = int(len(nums)/2)
        counter_dict = dict()
        for num in nums:
            if num not in counter_dict:
                counter_dict[num] = 1
            else:
                counter_dict[num] += 1
        return list(filter(lambda x: x[1] > beyond_counter, counter_dict.items()))[0][0]

    def majorityElement2(self, nums) -> int:
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        return x

    def majorityElement3(self, nums) -> int:
        n = len(nums)

        def quick_sort(nums, left, right):
            if left >= right:
                return nums
            i, j = left, right
            pivot = nums[i]
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[right] = pivot
            quick_sort(nums, i, left - 1)
            quick_sort(nums, left + 1, j)
            return nums

        nums = quick_sort(nums, 0, n - 1)
        print(nums)
        return nums[n // 2]


if __name__ == "__main__":
    solution = Solution()
    print(solution.majorityElement2([2,2,1,1,1,2,2]))
