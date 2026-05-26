from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1 
        res = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            res = max(res, area)

            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        
        return res
    
# time complexity: O(n)
# space complexity: O(1)