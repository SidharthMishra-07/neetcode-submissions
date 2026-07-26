class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = {}
        def solve(i):
            if i>=n:
                return 0
            if i not in dp:
                dp[i] = cost[i] + min(solve(i+1), solve(i+2))
            
            return dp[i]

        return min(solve(0), solve(1))
            
        