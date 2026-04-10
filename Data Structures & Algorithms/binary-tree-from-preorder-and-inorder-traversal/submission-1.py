# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if not preorder or not inorder:
        #     return None
        # root_val = preorder[0]
        # root = TreeNode(root_val)
        # root_index = inorder.index(root_val)
        # root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])
        # root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])
        # return root

        if not preorder or not inorder:
            return None
        inorder_map = {val:i for i,val in enumerate(inorder)}
        self.pre_idx = 0
        def dfs(left,right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            mid = inorder_map[root_val]
            root.left = dfs(left,mid-1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(inorder)-1)
        
        