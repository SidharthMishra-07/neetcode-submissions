import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        n = len(nums)
        self.k = k
        self.pq = []
        for i in range(n):
            heapq.heappush(self.pq, nums[i])
            if len(self.pq) > k:
                heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
            print(self.pq)
        elif self.pq[0] < val:
            heapq.heappushpop(self.pq, val)
        return self.pq[0]

        
        
