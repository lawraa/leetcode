from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        def backtrack(idx):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            
            # For one where we append
            subset.append(nums[idx])
            backtrack(idx+1)

            # For one where we don't append 
            subset.pop()
            backtrack(idx+1)
        
        backtrack(0)
        return res

# Time complexity: O(n*2^n)
# Space complexity: O(n) for subset