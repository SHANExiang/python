from collections import deque

# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。

# 示例1：
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1


class Solution(object):

    def coin_change(self, coins, amount):
        seen = {0}
        queue = deque([(0, 0)])
        while queue:
            cur, count = queue.popleft()
            if cur == amount:
                return count
            for i in coins:
                t = cur + i
                if t <= amount and t not in seen:
                    print((t, count+1))
                    queue.append((t, count+1))
                    seen.add(t)
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.coin_change([1, 2, 5], 11))
