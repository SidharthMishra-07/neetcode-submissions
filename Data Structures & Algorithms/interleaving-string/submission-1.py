class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #State: dp[i][j] = True if s3[0:i+j] is formed by the interleaving of s1[0:i] and s2[0:j]
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}

        def dfs(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))
            if (i, j) not in memo:
                memo[(i, j)] = False
                if i<len(s1) and s1[i] == s3[k]:
                    memo[(i, j)] = dfs(i+1, j, k+1)
                if j<len(s2) and s2[j] == s3[k]:
                    memo[(i, j)] = dfs(i, j+1, k+1)
            return memo[(i, j)]

        return dfs(0, 0, 0) 