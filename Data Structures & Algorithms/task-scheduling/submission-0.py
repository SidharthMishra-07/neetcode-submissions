class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # count is an hashmap
        maxheap = [-x for x in count.values()]
        heapq.heapify(maxheap)

        q = deque() # [-cnt, time+n]
        time = 0
        while maxheap or q:
            time +=1

            if maxheap:
                val = -heapq.heappop(maxheap) - 1 #reduce freq by 1
                if val:
                    q.append([-val, time+n]) 

            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        
        return time

#TC : nlogk
