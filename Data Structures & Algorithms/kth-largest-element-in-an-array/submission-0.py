class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for x in nums:
            heapq.heappush(minheap, x)
            if len(minheap) > k:
                heapq.heappop(minheap)
        return minheap[0]
