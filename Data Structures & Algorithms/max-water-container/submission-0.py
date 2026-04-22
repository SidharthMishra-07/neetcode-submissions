class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        res=0
        while l < r:
            area = min(height[l], height[r])*(r-l)
            res = max(area, res)
            if height[l] <= height[r]:
                l+=1
            elif height[l] > height[r]:
                r-=1
        return res