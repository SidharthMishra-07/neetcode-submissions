class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visit = [[False for _ in range(col)] for _ in range(row)]

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r<0 or c<0 or r>=row or c>=col or visit[r][c]==True or word[i]!=board[r][c]:
                return

            visit[r][c] = True
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            visit[r][c] = False

            return res 
            
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False