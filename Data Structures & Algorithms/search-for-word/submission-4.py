class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visit = [[False for _ in range(cols)] for _ in range(rows)]

        def backtrack(r, c, ch):
            if ch == len(word):
                return True
            if r not in range(rows) or c not in range(cols) or visit[r][c] == True or board[r][c] != word[ch]:
                return False
            
            visit[r][c] = True
            res = (backtrack(r+1, c, ch+1) or backtrack(r-1, c, ch+1) or backtrack(r, c+1, ch+1) or backtrack(r, c-1, ch+1))
            visit[r][c] = False
            
            return res

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
         