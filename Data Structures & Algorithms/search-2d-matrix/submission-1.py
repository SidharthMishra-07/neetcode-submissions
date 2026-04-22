class Solution:
    #Binary Search Solution
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        top=0; bot=row-1
        while top<=bot:
            r = (top+bot)//2
            if target > matrix[r][-1]:
                top+=1
            elif target < matrix[r][-1]:
                bot-=1
            else:
                break
        #now we have the row which contains the target
        start, end = 0, col-1

        while start <= end:
            mid = (start+end)//2
            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] > target:
                end = mid-1
            else:
                start = mid+1
        return False

        
