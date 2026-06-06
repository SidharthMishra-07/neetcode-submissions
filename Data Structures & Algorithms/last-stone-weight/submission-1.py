import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for x in stones:
            heapq.heappush(pq, -x)
        while pq:
            if len(pq) < 2:
                break
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            if x != y:
                heapq.heappush(pq, -abs(x-y))
        
        return -pq[0] if pq else 0
        