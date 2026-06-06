from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS Solution
        if not root:
            return 0
        
        from collections import deque
        res = 0
        q = deque([root])

        while q:
            res +=1
            for _ in range(len(q)):
                curr_node = q.popleft()
                if curr_node.left: q.append(curr_node.left)
                if curr_node.right: q.append(curr_node.right)
        
        return res

        # DFS Solution
        # if not root:
        #     return 0

        # res = 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
        # return res
    

# Time complexity: O(n)
# Space complexity: O(n)