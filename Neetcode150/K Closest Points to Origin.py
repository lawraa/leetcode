from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (dist,[x,y]))
        
        res = []

        while k >0:
            dist, point = heapq.heappop(heap)
            res.append(point)
            k = k-1
        
        return res

# Time Complexity: O(n log n)
# Space Complexity: O(n)
