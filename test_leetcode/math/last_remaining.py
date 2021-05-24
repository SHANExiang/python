

# 圆圈中最后剩下的数字
# 0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。
# 求出这个圆圈里剩下的最后一个数字。
#
# 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
# 示例 1：
#
# 输入: n = 5, m = 3
# 输出:3
# 示例 2：
#
# 输入: n = 10, m = 17
# 输出:2


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        def helper(lis, count):
            while len(lis) > 1:
                length = len(lis)
                if length == count:
                    lis.pop(-1)
                elif length > count:
                    lis.pop(count-1)
                    lis = lis[count-1:] + lis[0:count-1]
                else:
                    index = count % length - 1
                    if index == -1:
                        lis.pop(-1)
                    else:
                        lis.pop(index)
                        lis = lis[index:] + lis[0:index]

            return lis[0]
        return helper(list(range(n)), m)


if __name__ == "__main__":
    solution = Solution()
    print(solution.lastRemaining(88, 10))
