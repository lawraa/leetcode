# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution: 
    def checkMatch(self, curr_node, subRoot):
        p = deque([(curr_node, subRoot)])
        while p:
            curr, sub = p.popleft()
            if not curr and not sub:
                continue
            if not curr or not sub:
                return False
            if curr.val != sub.val:
                return False
            p.append((curr.left, sub.left))
            p.append((curr.right, sub.right))
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            curr_node = q.popleft()
            if curr_node.val == subRoot.val:
                found_match = self.checkMatch(curr_node, subRoot)
                if found_match:
                    return True
            
            if curr_node.left: q.append(curr_node.left)
            if curr_node.right: q.append(curr_node.right)
        
        return False

# Time complexity: O(n*m) 
# Space complexity: O(n+m)