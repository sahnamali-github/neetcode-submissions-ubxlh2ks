# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxV):
            if not node:
                return 0
            count = 0
            if node.val >= maxV:
                count = 1
            maxV = max(maxV, node.val)
            count += dfs(node.left, maxV)
            count += dfs(node.right, maxV)
            return count
        return dfs(root, root.val)

        