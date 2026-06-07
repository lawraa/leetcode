class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap) # largest
            second = -heapq.heappop(heap) # smaller

            if first != second:
                heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0

# Time Complexity: O(n log n)
# Space Complexity: O(n)