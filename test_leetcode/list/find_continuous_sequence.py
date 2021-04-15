

# 和为s的连续正数序列


class Solution:
    def findContinuousSequence(self, target: int):
        sum_seq = list()
        for i in range(1, target+1):
            sum_seq.append(sum(range(i)))
        print(sum_seq)
        res = list()
        for i in range(0, target):
            if (sum_seq[i] + target) in sum_seq:
                index = sum_seq.index(sum_seq[i] + target)
                tmp = [j for j in range(i+1, index+1)]
                res.append(tmp)
        return res

    def findContinuousSequence2(self, target: int):
        res = list()
        occur = dict()
        for i in range(target):
            occur[sum(range(i+1))] = i
        print(occur)
        for key, value in occur.items():
            if key+target in occur:
                index = occur.get(key+target)
                tmp = [j for j in range(value + 1, index + 1)]
                res.append(tmp)
        return res

    def findContinuousSequence3(self, target: int):
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j+1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.findContinuousSequence3(15))
