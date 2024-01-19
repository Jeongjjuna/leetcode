class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1
    
        while len(matrix) - 1 >= row and 0 <= col:
            if target == matrix[row][col]:
                return True
        
            if target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
                
        return False