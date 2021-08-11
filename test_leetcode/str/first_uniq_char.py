

"""
字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
"""


class Solution:
    def first_uniq_char(self, s: str) -> int:
        if len(s) == 1:
            return 0
        d = dict()
        for x in s:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1

        for i in range(len(s)):
            if s[i] in d and d[s[i]] == 1:
                return i
        return -1

    def first_uniq_char2(self, s):
        from collections import Counter
        frequency = Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1

    def first_uniq_char3(self, s: str) -> int:
        n = len(s)
        dic = dict()
        from collections import deque
        queue = deque()
        for index, ch in enumerate(s):
            if ch not in dic:
                dic[ch] = index
                queue.append((ch, index))
            else:
                dic[ch] = -1
                while queue and dic[queue[0][0]] == -1:
                    queue.popleft()
        return -1 if not queue else queue[0][1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.first_uniq_char("leetcode"))
    print(solution.first_uniq_char("loveleetcode"))
    print(solution.first_uniq_char("cc"))

