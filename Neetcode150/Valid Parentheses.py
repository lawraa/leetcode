class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        q = deque()

        pairs = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                q.append(s[i])
            else:
                if len(q) == 0:
                    return False
                temp = q.pop()

                if temp != pairs[s[i]]:
                    return False
        if len(q) == 0:
            return True
        return False

# Time complexity: O(n)
# Space complexity: O(n) 