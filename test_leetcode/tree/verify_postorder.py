

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
# 参考以下这颗二叉搜索树：
#
#      5
#     / \
#    2   6
#   / \
#  1   3
# 示例 1：
#
# 输入: [1,6,3,2,5]
# 输出: false
# 示例 2：
#
# 输入: [1,3,2,6,5]
# 输出: true


class Solution:

    def verifyPostorder(self, postorder) -> bool:
        def recur(left, right):
            if left >= right:
                return True
            p = left
            while postorder[p] < postorder[right]:
                p += 1
            m = p
            while postorder[p] > postorder[right]:
                p += 1
            return p == right and recur(left, m - 1) and recur(m, right - 1)
        return recur(0, len(postorder) - 1)


if __name__ == "__main__":
    solution = Solution()
    print(solution.verifyPostorder([4, 8, 6, 12, 16, 14, 10]))
