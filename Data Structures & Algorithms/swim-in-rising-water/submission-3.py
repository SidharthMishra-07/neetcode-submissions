class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dist = [[float("inf")] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        dist[0][0] = grid[0][0]
        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0))

        while pq:
            curr_dist, r, c = heapq.heappop(pq)

            if curr_dist > dist[r][c]:
                continue
            
            # if r == rows-1  and c == cols-1:
            #     return curr_dist

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr not in range(rows) or nc not in range(cols):
                    continue
                new_dist = max(curr_dist, grid[nr][nc])
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, nr, nc))
        
        return dist[rows-1][cols-1]