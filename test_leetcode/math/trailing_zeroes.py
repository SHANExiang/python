
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return  0
        def helper(num):
            if num == 1:
                return 1
            else:
                return num*helper(num-1)
        res = helper(n)
        count = 0
        while res % 10 == 0:
            count += 1
            res = res // 10
        return count

    def helper(self, num):
        if num == 1:
            return 1
        else:
            return num * self.helper(num - 1)

    def trailing_zeroes(self, n):
        print(self.helper(n))
        count = 0
        for i in range(5, n+1, 5):
            while i % 5 == 0:
                count += 1
                i = i // 5
        return count

    def trailing_zeroes1(self, n):
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.trailing_zeroes(35))
