
# 统计所有小于非负整数 n 的质数的数量。
#


class Solution:
    def countPrimes1(self, n: int) -> int:
        def is_primes(num):
            for i in range(2, num//2+1):
                if num % i == 0:
                    return False
            return True
        count = 0
        for i in range(2, n):
            if is_primes(i):
                print(i)
                count += 1
        return count

    # 使用标准的 埃拉托斯特尼 埃氏筛选法
    def countPrimes2(self, n: int) -> int:
        isNumPrimes = [True] * n  # 将所有数，展开所有数 标记质数真
        count = 0  # 质数计数器 因为1不是质数 所以 0
        # 遍历2，n 数，判断是否是质数，从2开始对应-质数3 [1,2,3]  1不算质数
        for i in range(2, n):
            if isNumPrimes[i]:
                count += 1
                # 使用埃拉托斯特尼 筛选法进行过滤 将合数去除
                for j in range(i * i, n, i):  # 遍历 i*i  2倍i值 开始，结束n, 步数i (倍数递增)
                    isNumPrimes[j] = False  # 把合数置为 False
        return count




if __name__ == "__main__":
    solution = Solution()
    print(solution.countPrimes2(78))