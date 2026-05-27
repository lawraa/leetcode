class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(s)):
            d[s[right]] += 1

            while (right-left+1) - max(d.values()) > k:
                d[s[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)
        
        return res

# Time Complexity: O(n)
# Space Complexity: O(1) since there are only 26 uppercase English letters
# or more general case O(m) where m is the size of the unique char in s