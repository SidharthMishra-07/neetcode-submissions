class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        minheap = [] #pair of (end, numpassengers)
        curpass = 0
        for numpass, start, end in trips:
            while minheap and minheap[0][0] <= start:
                curpass -= minheap[0][1]
                heapq.heappop(minheap)
            
            curpass += numpass
            if curpass > capacity:
                return False
            heapq.heappush(minheap, [end, numpass])
        
        return True


        