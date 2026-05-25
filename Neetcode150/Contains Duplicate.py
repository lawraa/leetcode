from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for num in nums:
            if num in x:
                return True
            x.add(num)
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)