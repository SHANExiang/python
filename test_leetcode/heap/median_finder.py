# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
#
# 例如，
#
# [2,3,4]的中位数是 3
#
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
# 设计一个支持以下两种操作的数据结构：
#
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
#

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = list()


    def addNum(self, num: int) -> None:
        self.nums.append(num)


    def findMedian(self) -> float:
        length = len(self.nums)
        self.nums.sort()
        if length % 2 == 0:
            return (self.nums[(length-1)//2] + self.nums[(length-1)//2 + 1])/2
        else:
            return self.nums[(length-1)//2]


class MedianFinder1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = list()
        self.B = list()

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heapq.heappush(self.A, num)
            heapq.heappush(self.B, -heapq.heappop(self.A))
        else:
            heapq.heappush(self.B, -num)
            heapq.heappush(self.A, -heapq.heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0


if __name__ == "__main__":
    find = MedianFinder1()
    find.addNum(3)
    find.addNum(4)
    find.addNum(2)
    find.addNum(7)
    find.addNum(9)
    find.addNum(1)
    find.addNum(10)
    find.addNum(6)
    find.addNum(5)
    print(find.A)
    print(find.B)
