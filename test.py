# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(root.left, root.right) + 1

    def max_depth(self, root):
        if not root:
            return 0
        queue, level = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            level += 1
        return level




if __name__ == "__main__":
    solution = Solution()
    print(solution.sumNums(3))