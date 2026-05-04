class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        res = 0

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                top = stack.pop()
                if len(stack)!=0:
                    curr = heights[top] * (i-stack[-1]-1)
                else:
                    curr = heights[top] * i
                
                res = max(res,curr)
            stack.append(i)

        while stack:
            top = stack.pop()
            if len(stack)!=0:
                curr = heights[top] * (n-stack[-1]-1)
            else:
                curr = heights[top] * n    
            res = max(res,curr)
        
        return res
