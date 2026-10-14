class MedianFinder:
    def __init__(self):
        self.maxheap = [] #Smaller Container
        self.minheap = [] #Greater Container

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)

        if self.maxheap and self.minheap and self.maxheap[0] > self.minheap[0]:
            val = - heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)

        if len(self.maxheap) > len(self.minheap):
            val = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)
        
        if len(self.minheap) > len(self.maxheap):
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            val1 = -self.maxheap[0]
            val2 = self.minheap[0]
            return (val1 + val2) / 2
        