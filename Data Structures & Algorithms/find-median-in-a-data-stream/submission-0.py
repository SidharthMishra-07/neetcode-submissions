class MedianFinder:
    def __init__(self):
        self.maxheap=[] #Smaller Container
        self.minheap=[] #Greater Container

    def addNum(self, num: int) -> None:
        #Adding first element to maxheap by default
        heapq.heappush(self.maxheap, -num)

        #Putting value from maxheap to minheap if value pushed was supposed to be in minheap
        if self.maxheap and self.minheap and self.maxheap[0] > self.minheap[0]:
            val = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)

        #Balancing the sizes
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
            return (-self.maxheap[0] + self.minheap[0]) / 2
        
        