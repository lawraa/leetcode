class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        
        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            bucket[freq].append(num)
        
        res = []

        for freq in range(len(nums), 0, -1):
            for f in bucket[freq]:
                res.append(f)
                k -= 1
            
            if k == 0:
                return res

# Time Complexity: O(n)
# Space Complexity: O(n)