import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in range(k):
            heapq.heappush(pq, nums[i])
        for i in range(k, len(nums)):
            heapq.heappushpop(pq, nums[i])
        return pq[0]