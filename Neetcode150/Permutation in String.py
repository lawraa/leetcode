class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Initial Approch
        # from collections import defaultdict
        # d = defaultdict(int)
        # for char_s1 in s1:
        #     d[char_s1] += 1
        
        # left = 0
        # k = len(s1)

        # for right in range(k-1, len(s2), 1):
        #     d_copy = d.copy()
        #     for i in range(left, right+1, 1):
        #         if d_copy[s2[i]] > 0:
        #             d_copy[s2[i]] -= 1
        #         else:
        #             left += 1
        #             break
        #     if max(d_copy.values()) == 0:
        #         return True
        
        # return False
    
    # Better Time/Space Complexity
        k = len(s1)
        s1_arr = [0]*26
        s2_arr = [0]*26
        
        if len(s2) < len(s1): return False
        for i in range(k):
            s1_arr[ord(s1[i]) - ord('a')] += 1
            s2_arr[ord(s2[i]) - ord('a')] += 1
        
        if s1_arr == s2_arr: return True

        for j in range(k, len(s2)):
            s2_arr[ord(s2[j]) - ord('a')] += 1
            s2_arr[ord(s2[j-k]) - ord('a')] -= 1
            if s1_arr == s2_arr: return True
        
        return False
    
    # Time Complexity: O(n) where n is the length of s2
    # Space Complexity: O(1) since there are only 26 lowercase English letters