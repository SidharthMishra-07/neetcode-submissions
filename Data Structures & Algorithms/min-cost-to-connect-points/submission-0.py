class DSU:
    def __init__(self, V) -> None:
        self.parent = list(range(V))
        self.rank = [0] * V
    
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x]) # path compression
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        if self.rank[py] < self.rank[px]:
            self.parent[py] = px
        else:
            self.parent[px] = py
            self.rank[px] +=1
        
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = []
        cost = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((i, j, dist))

        edges.sort(key = lambda x: x[2])
        for u, v, wt in edges:
            if dsu.union(u,v) == True:
                cost+=wt

        return cost

            
