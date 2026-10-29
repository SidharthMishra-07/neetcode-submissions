class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))

        res = ""
        count = 1

        if not pq:
            return ""

        while pq:
            num, char = heapq.heappop(pq)
            num = -num

            if res!="" and res[-1] == char:
                count+=1
            else:
                count = 1

            if count == 3:
                # If there is no second character available,
                if not pq:
                    return res

                num2, char2 = heapq.heappop(pq)
                num2 = -num2

                res+=char2
                num2 = num2-1

                if num2!=0:
                    heapq.heappush(pq, (-num2, char2))
                
                # Current char was not used, so push it back unchanged
                heapq.heappush(pq, (-num, char))

                count = 1
                continue

            res+= char
            num = num-1

            if num!=0:
                heapq.heappush(pq, (-num, char))
        
        return res
        