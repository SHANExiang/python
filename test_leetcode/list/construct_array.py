

# 给定一个数组A[0,1,…,n-1]，请构建一个数组B[0,1,…,n-1]，其中B[i]的值是数组A中除了下标i以外的元素的积,
# 即B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
#
# 示例:
#
# 输入: [1,2,3,4,5]
# 输出: [120,60,40,30,24]
#
# 提示：
#
# 所有元素乘积之和不会溢出32位整数
# a.length <= 100000
#
# 1 2 3 4 5
#1 1
#2  1
#3    1
#4      1
#5        1


class Solution:
    def constructArr(self, a):
        res = []
        j, n = 0, len(a)
        while j < n:
            ele = 1
            for i in range(n):
                if i != j:
                    ele *= a[i]
            res.append(ele)
            j += 1
        return res

    def construct_array(self, a):
        res, n = [1]*len(a), len(a)
        for i in range(1, n):
            res[i] = res[i-1]*a[i-1]
        tmp = 1
        for j in range(n-2, -1, -1):
            tmp *= a[j+1]
            res[j] = res[j]*tmp
        return res


if __name__ == "__main__":
    solution = Solution()
    solution.construct_array([1,2,3,4,5])