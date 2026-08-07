class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #State: memo[i][j] = number of ways to make j amount using i coins
        n = len(coins)
        memo = [[-1] * (amount+1) for _ in range(n+1)]

        def dfs(i, j):
            if j == 0:
                return 1
            if i>=n or j<0:
                return 0
            if memo[i][j] == -1:
                memo[i][j] = dfs(i, j-coins[i]) + dfs(i+1, j)
            return memo[i][j]
        
        return dfs(0, amount)