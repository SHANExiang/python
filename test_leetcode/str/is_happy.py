

# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」定义为：
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为1，那么这个数就是快乐数。
# 如果 n 是快乐数就返回 true ；不是，则返回 false 。
# 关键点------无限循环的n肯定有相同的值


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            # n = str(num)
            # sum_n = 0
            # for i in n:
            #     sum_n += pow(int(i), 2)
            total_sum = 0
            while num > 0:
                mod = num % 10
                num = num // 10
                total_sum += mod * mod
            return total_sum
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        print(seen)
        return n == 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.isHappy(2))
