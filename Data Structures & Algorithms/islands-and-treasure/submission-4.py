class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0]) 
        visited = set()
        INF = 2147483647
        steps = 1
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            for _ in range(len(q)):
                row,col = q.popleft()
                directions = [(1,0),(0,1),(-1,0),(0,-1)]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == INF:
                        grid[r][c] = steps
                        q.append((r,c))
                        # visited.add((r,c))

            steps+=1
