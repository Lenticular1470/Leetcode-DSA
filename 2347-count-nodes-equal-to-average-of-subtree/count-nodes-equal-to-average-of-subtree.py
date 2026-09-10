# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.c = 0
        def dfs(node):
            if not node:
                return 0, 0
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)

            tots = node.val + ls + rs
            totc = 1 + lc + rc

            avg = tots // totc

            if node.val == avg:
                self.c += 1
            return tots, totc
        dfs(root)
        return self.c

        