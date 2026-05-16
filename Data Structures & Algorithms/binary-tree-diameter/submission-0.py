# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        #return height
        def dfs(node):
            if not node:
                return 0
            lh = dfs(node.left)   
            rh = dfs(node.right) 
            
            self.res = max(self.res, lh+rh)
            return max(lh, rh) + 1    

        dfs(root)
        return self.res