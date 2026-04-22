class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minVal = prices[0]
        for x in prices:
            minVal = min(minVal, x)
            res = max(res, x-minVal)
        return res