

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(1, n+1):
            a, b = b, a + b
        return a % (pow(10, 9) + 7)


if __name__ == "__main__":
    solution = Solution()
    print(solution.fib(45))
