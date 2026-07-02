class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        time = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))

        while fresh>0 and q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in [[-1,0], [1,0], [0,-1], [0,1]]:
                    r, c = row+dr, col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -=1
                        q.append((r,c))
            time+=1
        return time if fresh == 0 else -1