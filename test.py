# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


class Solution:
    def majorityElement(self, nums) -> int:
        tmp_dict = dict()
        for num in nums:
            if num not in tmp_dict:
                tmp_dict[num] = 1
            else:
                tmp_dict[num] += 1
        tmp_dict = sorted(tmp_dict.items(), key=lambda x: x[1])
        return tmp_dict[-1][1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))