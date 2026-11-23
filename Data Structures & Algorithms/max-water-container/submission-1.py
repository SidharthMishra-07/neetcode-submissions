class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) - 1
        res = 0
        ans = 0
        while low < high:
            dist = high-low
            res = dist * min(heights[low], heights[high])
            if heights[low] <= heights[high]:
                low+=1
            else:
                high-=1
            ans = max(ans, res)
        return ans 