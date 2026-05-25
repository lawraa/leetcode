from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeros = 0
        for num in nums:
            if num != 0:
                total = total * num
            else:
                zeros += 1
        res = []
        if zeros > 1:
            res = [0] * len(nums)
        elif zeros == 1:
            for num in nums:
                if num == 0:
                    res.append(int(total))
                else:
                    res.append(0)
        else:
            for i, num in enumerate(nums):
                res.append(int(total/nums[i]))
        return res

# Time Complexity: O(n)
# Space Complexity: O(n)

# Follow up: Can you solve it without division and in O(n)?

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
    
# Time Complexity: O(n)
# Space Complexity: O(n)