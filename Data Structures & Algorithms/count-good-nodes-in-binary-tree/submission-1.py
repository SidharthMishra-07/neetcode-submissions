# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: 
            return 0
        q = deque()
        q.append((root, float('-inf')))
        count = 0

        while q:
            node, maxval = q.popleft()

            if node.val >= maxval:
                count+=1
                maxval = max(maxval, node.val)
            if node.left:
                q.append((node.left, maxval))
            if node.right:
                q.append((node.right, maxval))

        return count