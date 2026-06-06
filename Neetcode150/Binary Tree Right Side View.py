from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        from collections import deque

        q = deque([root])
        res = []
        while q:
            level_node = len(q)
            for i in range(level_node):
                node = q.popleft()
                if i == level_node - 1:
                    res.append(node.val)
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
        return res

# Time complexity: O(n)
# Space complexity: O(n)