class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)
        minK = 1
        res = maxK
        while minK <= maxK:
            k = (minK+maxK)//2
            hour=0
            for x in piles:
                hour+=math.ceil(float(x)/k)
            if hour <= h:
                res = k
                maxK = k-1
            else:
                minK = k+1
        return res