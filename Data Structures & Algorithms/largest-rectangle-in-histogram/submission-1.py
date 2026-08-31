class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                top = stack.pop()
                if stack:
                    curr = heights[top] * (i-1 - stack[-1])
                else:
                    curr = heights[top] * i
                res = max(res, curr)
            stack.append(i)
        
        while stack:
            top = stack.pop()
            if stack: 
                curr = heights[top] * (n-1 - stack[-1])
            else:
                curr = heights[top] * n
            res = max(res, curr)
        
        return res
        