class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        res = high
        while low<=high:
            mid = (low+high)//2
            cap = mid
            count = 1

            for w in weights:
                if cap - w < 0:
                    count+=1
                    cap = mid
                
                cap -= w
            if count <= days:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res
