import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.k = k
        for i in range(len(nums)):
            heapq.heappush(self.minheap, nums[i])
            if len(self.minheap) > k:
                heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        elif self.minheap[0] < val:
            heapq.heappushpop(self.minheap, val)
        return self.minheap[0]
