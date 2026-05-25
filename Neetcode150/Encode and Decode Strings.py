from typing import List 

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)) + "#" + s)

        return "".join(res)
        
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        
        while i < len(s):
            temp = ""
            j = i
            while s[j] != "#":
                temp += s[j]
                j+= 1
            
            res.append(s[j+1:j+1+int(temp)])
            i = j+int(temp)+1
        return res
# Encode:
# Time Complexity: O(n)
# Space Complexity: O(n)

# Decode:
# Time Complexity: O(n)
# Space Complexity: O(n)