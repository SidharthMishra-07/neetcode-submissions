class Solution:
    #Heap Solution
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        
        heap = []
        for x in freq:
            heapq.heappush(heap, (freq[x], x))  #(value, key) pair 
            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
        