class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def bfs(r, c):
            visited.add((r,c))
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r1, c1 = row+dr, col+dc
                    if r1 in range(rows) and c1 in range(cols) and grid[r1][c1] == "1" and (r1,c1) not in visited:
                        q.append((r1, c1))
                        visited.add((r1, c1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands+=1
        
        return islands

        