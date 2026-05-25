class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        # row check and column check 
        
        n = len(board[0])
        
        for i in range(n):
            row_set = set()
            column_set = set()
            for j in range(n):
                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                    else: 
                        row_set.add(board[i][j])
            
                if board[j][i] != ".":
                    if board[j][i] in column_set:
                        return False
                    else: 
                        column_set.add(board[j][i])
        # kernel check
        for box_row in range(0, n, 3):
            for box_column in range(0, n, 3):
                box_set = set()
                for i in range(3):
                    for j in range(3):
                        row = i+box_row
                        column = j+box_column
                        if board[row][column] != ".":
                            if board[row][column] in box_set:
                                return False
                            else:
                                box_set.add(board[row][column])
        
        return True

# Time Complexity: O(n^2)
# Space Complexity: O(n) # for row_set, column_set, box_set             