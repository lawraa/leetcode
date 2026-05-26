class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLen = 1
        letter_set = set()
        left = 0
        letter_set.add(s[0])
        for i in range(1, len(s), 1):
            if s[i] in letter_set:
                while s[left] != s[i]:
                    letter_set.remove(s[left])
                    left+=1
                left+=1
            else:
                letter_set.add(s[i])
                maxLen = max(maxLen, i - left + 1)
        
        return maxLen

# Time Complexity: O(n)
# Space Complexity: O(m) where m is the size of the unique characters of the input string