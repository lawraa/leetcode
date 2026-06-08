from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = nums[:k] # first k nums
        heapq.heapify(heap)

        for num in nums[k:]:
            if num>heap[0]:
                heapq.heappushpop(heap, num)
        
        return heap[0]

# Time Complexity: O(n log k)
# Space Complexity: O(k)
