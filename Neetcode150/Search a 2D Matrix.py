from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        m = len(matrix)

        left = 0
        right = (m*n) - 1

        while left <= right:
            mid = (left+right+1)//2 
            i = int(mid/n)
            j = mid%n

            num = matrix[i][j]
            if num > target:
                right = mid - 1
            elif num < target:
                left = mid + 1
            else: 
                return True
        
        return False

# Time complexity: O(log(mn))
# Space complexity: O(1)