class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxx = max(max(row) for row in grid)
        minn = min(min(row) for row in grid)

        def dfs(r, c, t, visited):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or grid[r][c] > t:
                return False
            if r == rows-1 and c == cols-1:
                return True

            visited.add((r,c))
            return (dfs(r + 1, c, t, visited) or
                    dfs(r - 1, c, t, visited) or
                    dfs(r, c + 1, t, visited) or
                    dfs(r, c - 1, t, visited))

        l, r = minn, maxx
        while l < r:
            visited = set()
            m = (l+r) // 2
            if dfs(0, 0, m, visited):
                r = m
            else:
                l = m + 1

        return r