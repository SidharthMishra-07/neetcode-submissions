class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        top, bot = 0, row-1

        while top<=bot:
            r = (top+bot)//2
            if target > matrix[r][-1]:
                top = r+1
            elif target < matrix[r][0]:
                bot = r-1
            else:
                break  # row found

        #now search column
        start, end = 0, col-1
        while start<=end:
            c = (start+end)//2
            if target == matrix[r][c]:
                return True
            if matrix[r][c] < target:
                start = c+1
            else:
                end = c-1
        return False 
