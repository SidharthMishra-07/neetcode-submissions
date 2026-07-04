class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [0] * (n+1)
        res = []

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            
            if px == py:
                return False

            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[py] < rank[px]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
        
        for u, v in edges:
            if union(u,v) == False:     #Meaning they are already connected
                res = [u, v]

        return res
            