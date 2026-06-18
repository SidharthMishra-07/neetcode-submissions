class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or
                c >= cols or grid[r][c] == "0" or (r,c) in visited):
                return

            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                dfs(r+dr, c+dc)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    islands+=1

        return islands