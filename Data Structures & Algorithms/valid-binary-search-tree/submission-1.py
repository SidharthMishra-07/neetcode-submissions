# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        def isBST(node):
            nonlocal prev
            if not node:
                return True
            if isBST(node.left) == False:
                return False
            if node.val <= prev:
                return False
            prev = node.val
            return isBST(node.right)

        ans = isBST(root)
        return ans
