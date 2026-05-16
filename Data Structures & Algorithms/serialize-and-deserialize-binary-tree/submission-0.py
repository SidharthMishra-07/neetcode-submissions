# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
               res.append("N")
            if node:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(",")
        self.count = 0

        def dfs():
            if self.count == len(val):
                return None

            ele = val[self.count]
            self.count+=1

            if ele == "N":
                return None
            
            root = TreeNode(int(ele))
            root.left = dfs()
            root.right = dfs()

        return root