

class Solution:
    def search(self, nums, target: int) -> int:
        res = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left)//2
            if target == nums[mid]:
                i, j = mid, mid + 1
                while 0 <= i:
                    if target == nums[i]:
                        i -= 1
                        res += 1
                    else:
                        break
                while j < len(nums):
                    if target == nums[j]:
                        j += 1
                        res += 1
                    else:
                        break
                break
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([5], 5))
