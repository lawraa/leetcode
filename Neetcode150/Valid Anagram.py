
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # from collections import Counter
        # if Counter(s) == Counter(t):
        #     return True
        # return False

        # Without using Counter
        if len(s) != len(t):
            return False

        arr = [0] * 26
        for i in range(len(s)):
            arr[ord(s[i])-ord("a")]+=1
            arr[ord(t[i])-ord("a")]-=1

        for a in arr:
            if a != 0:
                return False

        return True
    
# Time Complexity: O(n+m)
# Space Complexity: O(1) # only 26 lowercase letters