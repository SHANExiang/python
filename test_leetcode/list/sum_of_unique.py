

# 给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。
# 请你返回 nums 中唯一元素的和 。
class Solution(object):
    def sumOfUnique(self, nums) -> int:
        dic = dict()
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        return sum(dict(filter(lambda x: x[1] == 1, dic.items())).keys())


if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfUnique([1,2,2,2,5]))
