class Solution:
    # Mark the O that are not surrounded as T and convert everything to X
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def capture(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] != 'O':
                return

            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Capture unsurrounded regions O -> T (ie; O at the borders)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows-1] or c in [0, cols-1]):   #Border cells
                    capture(r, c)

        # Make everything O -> X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # Make All T->O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'


