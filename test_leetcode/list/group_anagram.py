

# 49. 字母异位词分组
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：
#
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。


class Solution:
    # 超时
    def groupAnagrams(self, strs):
        def is_anagram(s1, s2):
            if len(s1) != len(s2):
                return False
            from collections import Counter
            return Counter(s1) == Counter(s2)
        res = []
        while strs:
            n = len(strs)
            if n == 1:
                res.append(strs)
                break
            i, j = 0, 1
            tmp = []
            tmp.append(strs[0])
            while j < len(strs):
                if is_anagram(strs[i], strs[j]):
                    tmp.append(strs.pop(j))
                else:
                    j += 1
            strs.pop(0)
            res.append(tmp)
        return res

    def group_anagrams1(self, strs):
        from collections import defaultdict
        mp = defaultdict(list)
        for st in strs:
            key = ''.join(sorted(st))
            mp[key].append(st)
        return list(mp.values())

    def group_anagrams2(self, strs):
        from collections import defaultdict
        mp = defaultdict(list)
        for st in strs:
            counts = [0]*26
            for ch in st:
                counts[ord(ch) - ord('a')] += 1
            mp[tuple(counts)].append(st)
        return list(mp.values())


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["c", "c",]))
