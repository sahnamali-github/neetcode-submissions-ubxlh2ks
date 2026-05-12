class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def height(node):
            if not node:
                return 0
            leftHeight = height(node.left)
            rightHeight = height(node.right)
            if abs(leftHeight - rightHeight) > 1:
                self.balanced = False
            return 1 + max(leftHeight, rightHeight)
        height(root)
        return self.balanced