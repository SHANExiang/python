

# 50. Pow(x, n)
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。
#
#
#
# 示例 1：
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 示例 2：
#
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 示例 3：
#
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25
#
#
# 提示：
#
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# -104 <= xn <= 104


class Solution:
    # 超时
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        if n < 0:
            for _ in range(-n):
                res *= 1/x
        elif n > 0:
            for _ in range(n):
                res *= x
        else:
            res = 1
        return res

    def my_pow(self, x, n):
        def quick_mul(N):
            if N == 0:
                return 1
            y = quick_mul(N//2)
            return y*y if N%2==0 else y*y*x
        return quick_mul(n) if n > 0 else 1/quick_mul(-n)

    def my_pow2(self, x, n):
        def quick_mul(N):
            if N == 0:
                return 1
            res = 1
            x_contribute = x
            while N > 0:
                if N % 2 == 1:
                    res *= x_contribute
                x_contribute *= x_contribute
                N // 2
            return res
        return quick_mul(n) if n > 0 else 1/quick_mul(-n)
