from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        min_num = 1000
        while left < right:
            mid = (left+right)//2
            if nums[left] < nums[right]:
                return nums[left]
            
            if nums[mid] < nums[left] and nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[left] and nums[mid] > nums[right]:
                left = mid + 1
            else: 
                return nums[right]
        return nums[right]

# Time Complexity: O(log n)
# Space Complexity: O(1)
