# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Method 1 
        # if not preorder or not inorder:
        #     return None
        # root_val = preorder[0]
        # root = TreeNode(root_val)
        # root_idx = inorder.index(root_val)
        # root.left = self.buildTree(preorder[1:root_idx + 1], inorder[:root_idx])
        # root.right = self.buildTree(preorder[root_idx + 1:], inorder[root_idx + 1:])
        # return root

        #Method 2
        if not preorder or not inorder:
            return None
        self.pre_idx = 0
        index_map = {val:i for i,val in enumerate(inorder)}
        def dfs(left,right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            root_idx = index_map[root_val]

            root.left = dfs(left, root_idx - 1)
            root.right = dfs(root_idx + 1,right)
            return root
        return dfs(0, len(inorder)-1)
            

        




        