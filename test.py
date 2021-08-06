

class Solution:
    def singleNumber(self, nums) -> int:
        from collections import Counter
        counter = Counter(nums)
        for key, value in counter.items():
            if value == 1:
                return key
        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([9,1,7,9,7,9,7]))
