import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x, y in points:
            dist.append(float(math.sqrt((x-0)**2 + (y-0)**2)))
        
        pq = []
        for i in range(len(dist)):
            heapq.heappush(pq, (dist[i], i))
        
        res=[]
        for _ in range(k):
            d, idx = heapq.heappop(pq)
            res.append(points[idx])
        return res