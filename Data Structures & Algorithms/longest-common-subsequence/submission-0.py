class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dfs(m, n):
            if m == len(text1) or n == len(text2):
                return 0
            if (m, n) not in memo:
                if text1[m] == text2[n]:
                    memo[(m, n)] = 1 + dfs(m+1, n+1)
                else:
                    memo[(m, n)] = max(dfs(m+1, n), dfs(m, n+1))

            return memo[(m, n)]
        
        return dfs(0, 0)