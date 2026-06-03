# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIndex = 0
        def convert(preorder, inorder, s, e):
            nonlocal preIndex
            if s > e:
                return None
            root = TreeNode(preorder[preIndex])
            preIndex+=1

            inIndex = s
            for i in range(s, e+1):
                if inorder[i] == root.val:
                    inIndex = i
                    break
            
            root.left = convert(preorder, inorder, s, inIndex-1)
            root.right = convert(preorder, inorder, inIndex+1, e)

            return root

        node = convert(preorder, inorder, 0, len(preorder)-1)
        return node


