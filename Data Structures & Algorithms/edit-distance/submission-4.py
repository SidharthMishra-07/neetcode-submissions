class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(m, n):
            if n == 0: 
                return m
            if m == 0:
                return n
            if (m, n) not in memo:
                if word1[m-1] == word2[n-1]:
                    memo[(m, n)] = dfs(m-1, n-1)
                else:
                    memo[(m, n)] = 1 + min(dfs(m, n-1), dfs(m-1, n), dfs(m-1, n-1)) #insert, delete, update resp
            return memo[(m, n)]
        
        return dfs(len(word1), len(word2))