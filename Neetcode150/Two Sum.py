from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # for i in range(n):
        #     temp = target - nums[i]
        #     for j in range(i+1, n):
        #         if nums[j] == temp:
        #             return [i, j]
         
        # Time complexity: O(n^2)
        # Space complexity: O(1)

        a = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in a:
                return [a[temp], i]
            
            a[nums[i]] = i

        # Time complexity: O(n)
        # Space complexity: O(n)
            
                
                

