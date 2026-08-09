class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if n > m:
            return 0
        memo = {}

        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            if (i, j) not in memo:
                if s[i] == t[j]:
                    memo[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j)
                else:
                    memo[(i, j)] = dfs(i+1, j)
            return memo[(i, j)]

        return dfs(0, 0)