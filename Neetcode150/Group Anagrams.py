from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        # def checkAnagrams(s: str, t:str) -> bool:
        #     if len(s) != len(t):
        #         return False
        #     count = [0] * 26
        #     for i in range(len(s)):
        #         count[ord(s[i]) - ord("a")] += 1
        #         count[ord(t[i]) - ord("a")] -= 1
        #     for c in count:
        #         if c != 0:
        #             return False
        #     return True

        # res = []
        
        # for s in strs:
        #     new_group = True
        #     for r in res:
        #         if checkAnagrams(s,r[0]):
        #             r.append(s)
        #             new_group = False
        #             break
        #     if new_group:
        #         res.append([s])
              
        # return res
        
        # Time complexity: O(n^2 * m)
        # Space complexity: O(n * m) # n is number of strings, m is length of longest string

        from collections import defaultdict
        group = defaultdict(list)
        for s in strs:
            count = [0]*26
            for letter in s:
                count[ord(letter) - ord("a")]+=1
            key = tuple(count)
            group[key].append(s)
        
        return list(group.values())

        # Time complexity: O(n * m)
        # Space complexity: O(n * m) # n is number of strings, m is length of longest string
