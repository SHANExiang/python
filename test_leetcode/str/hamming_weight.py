

# 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。


class Solution:
    def hammingWeight(self, n: int) -> int:
        # n = str(n)
        count = 0
        for i in n:
            print(i)
            if int(i) == 1:
                count += 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingWeight("00000000000000000000000000001011"))
