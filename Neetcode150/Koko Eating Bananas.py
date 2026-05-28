class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n == h:
            return max(piles)

        low = 1
        high = max(piles)
        lowest = high

        while low <= high:
            mid = (low+high)//2
            count = 0
            for i in range(n):
                temp = -(-piles[i]//mid)
                count += temp
            
            if count > h:
                low = mid + 1
            elif count <= h:
                high = mid - 1
                lowest = mid            
        return lowest
            
# Time complexity: O(n log m)
# Space complexity: O(1)
