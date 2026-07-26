class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def solve(i):
            if i >= n:
                return i == n
            if i not in dp:
                dp[i] = solve(i+1) + solve(i+2)
            return dp[i]
        return solve(0)
