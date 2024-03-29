

# 56. 合并区间
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
# 请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
#
#
#
# 示例 1：
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].


class Solution:
    def merge(self, intervals):
        n = len(intervals)
        if n == 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        i, res = 0, []
        while i < n:
            if i == 0 or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            i += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([[1,4]]))