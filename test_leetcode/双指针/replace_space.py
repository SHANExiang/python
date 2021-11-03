

# 请实现一个函数，把字符串s中的每个空格替换成"%20"。
# 输入：s = "We are happy."
# 输出："We%20are%20happy."


class Solution:
    def replaceSpace(self, s: str) -> str:
        return "%20".join(s.split(' '))

    # 其实很多数组填充类的问题，都可以先预先给数组扩容带填充后的大小，然后在从后向前进行操作。
    def replace_space(self, s):
        count = 0
        for ch in s:
            if ch == ' ':
                count += 1
        n = len(s)
        res = list(s)
        res.extend([" "] * 2 * count)
        left, right = n - 1, len(res) - 1
        while 0 <= left <= right:
            if res[left] == ' ':
                res[right-2:right+1] = '%20'
                right -= 3
                left -= 1
            else:
                res[right] = res[left]
                right -= 1
                left -= 1
        return ''.join(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.replace_space('We are happy.'))
