class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prevheight):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or heights[r][c] < prevheight:
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
        
        #Adding first and last row borders to pacific and atlantic resp:
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])
        
        #Adding first and last col to pacific and Atlantic resp
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])
        
        res = []

        #Check for values present in both pacific and atlantic sets
        for (r,c) in pacific:
            if (r,c) in atlantic:
                res.append((r,c))

        return res