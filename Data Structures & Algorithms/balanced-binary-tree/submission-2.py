class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def height(node):
            if not node:
                return 0
            leftHeight = height(node.left)
            rightHeight = height(node.right)
            if leftHeight is False or rightHeight is False or abs(leftHeight - rightHeight) > 1:
                return False
            return 1 + max(leftHeight, rightHeight)
        
        return height(root) is not False