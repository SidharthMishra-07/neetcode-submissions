import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        res = []
        for point in points:
            x1 = point[0]
            y1 = point[1]
            dist.append(float(math.sqrt((x1 - 0)**2 + (y1 - 0)**2)))
        pq = []
        for i in range(len(dist)):
            heapq.heappush(pq, (dist[i], i))

        for _ in range(k):
            ele, idx = heapq.heappop(pq)
            res.append(points[idx])
            
        return res

