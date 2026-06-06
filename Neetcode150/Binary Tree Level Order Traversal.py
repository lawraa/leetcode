from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        res = []
        q = deque([root])

        while q:
            curr_level = []
            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(curr_level)

        return res
            
            
# Time complexity: O(n)
# Space complexity: O(n)
