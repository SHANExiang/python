from collections import Counter


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


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        res = float('inf')

        def dfs(index, path):
            if sum(path) > amount:
                return
            elif sum(path) == amount:
                print(path)
                nonlocal res
                if len(path) < res:
                    res = len(path)
                return
            path.append(coins[index])
            for i in range(len(coins)):
                import copy
                p = copy.deepcopy(path)
                dfs(i, p)
                p.pop()
        path = []
        dfs(0, path)
        return int(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))
